import pandas as pd
import numpy as np
import os
from collections import defaultdict
import logging
# from sqlalchemy.engine.base import Engine
import gc
# import MySQLdb
import datetime


class RhQuant:
    """
    量化投资系统框架
    """

    def __init__(self):
        """
        初始化策略
        :param init_log:默认True，如果不想在初始化的时候加载日志，请设为False
        """
        '''necessary, 以下变量必须在子类重写'''
        self.start_time: str = ''  # str 回测的初试时间, 如: '2015-01-01'
        self.end_time: str = ''  # str 回测的终止时间, 如: '2018-01-01'
        self.capitalStart: int = 1e6  # 初始化资金量
        self.strategyName: str = 'test_strategy'  # 策略名称
        self.timeEndFlag: str = ''  # 记录高频数据每天最后一个交易时刻的标记，若数据为日度数据，可设置为：''，若数据为高频数据，一般设置为'15:00:00'

        '''options, 以下变量可以根据实际情况在子类重写'''
        self.col_code: str = 'code'  # 设置DataFrame中代码列的col_name
        self.col_date: str = 'date'  # 设置DataFrame中日期列的col_name
        self.dealType: str = 'close'  # 实际成交与持仓的价格类型，一般为close。
        self.plotMode: str = 'plotly'  # 有'pyqt'和'plotly'两种可视化输出模式，大小写不限。
        self.pathSaveDirName: str = 'out'  # 输出结果存储目录
        self.marginRatio: float = 0.0  # 保证金比率，适用于衍生品
        self.contractUnit: int = 1e4  # 合约乘数，适用于衍生品：期权为1e4，期货为300.
        self.riskFreeRatio: float = 0.03  # 无风险利率
        self.colDropList: list = ['high', 'low', 'open']  # 设置在tradeFlow中要删除的一些列表
        self.strategyVarList: list = [20, 40]  # 策略所使用的变量，暂时无用，未来可能会用到。
        # self.logInitDefault: bool = True  # 是否使用默认的日志初始化。
        self.logOutput: bool = True  # bool 用于设置是否输出交易结果日志。
        self.logSaveDir: str = 'log'  # log的存储文件夹

        '''forbid, 以下变量禁止在子类重写'''
        # 设置日志
        # if init_log is True:
        #     self._init_log()

        # 持仓
        self.posFullDict: dict = {}  # 记录股票组合的持有信息。形式为：{countOpen:posDict}
        self.posDict: dict = {}  # 记录当前时刻的 posDict 信息
        self.posValSer: pd.Series = pd.Series([0] * 6, index=['date', 'val', 'secVal', 'cash', 'valRate', 'fee'])  # 存放持仓的资金信息。
        self.posValList: list = []  # 存储交易流水的每日汇总
        self.posValDF: pd.DataFrame = pd.DataFrame()  # 存储交易流水的每日汇总

        # 交易
        self.countOpen = self.countClose = self.countClear = 0  # 开平清仓组合触发次数记录
        self.tradeFlowList: list = []  # 存储交易流水
        self.tradeFlowDF: pd.DataFrame = pd.DataFrame()  # 存储交易流水
        self.tradeDict: defaultdict = defaultdict(lambda: 0)  # 用户持有的股票资产数据
        self.feeTimeList: list = []  # list 记录一个交易时刻所产生的交易手续费。
        self.workDayNum: int = 0  # int 记录交易日的个数。

        # 绘图
        self.plotDataList: list = []  # list 传递给绘图的数据，用来plot输出

        # 数据存储
        self.secCodeList: list = []  # list csv数据源特有变量，存储代码列表
        self.secDataDict: dict = {}  # dict csv数据源特有变量，形式为：{code:df}
        self.df_data: pd.DataFrame = pd.DataFrame()  # DataFrame 存储数据源

        # 指标计算
        self.valMaxDown: float = 0.0  # float 记录最大回撤
        self.valMaxDownPeriods: int = 0  # int 记录最长回撤的天数
        self.valIdxMax = None  # Timestamp() 记录回撤的最高点位时间
        self.valIdxMaxStr: str = ''  # str 记录回撤的最高点位时间,本质是str(valIdxMax)
        self.valMax: float = 0.0  # float 记录回撤的最高点位
        self.valMin: float = 0.0  # float 记录回撤的最低点位
        self.capitalProfit: float = 0.0  # float 记录资产的总盈亏
        self.capitalEnd: float = 0.0  # float 记录资产的最终值
        self.posValDFBus: pd.DataFrame = pd.DataFrame()  # DataFrame 存放posValDF的 Business频率的数据
        self.returnRateAvg: float = 0.0  # float 记录资产的年化收益率
        self.returnRateStd: float = 0.0  # float 记录资产的年化标准差
        self.returnRateSharp: float = 0.0  # float 记录资产的夏普比
        self.returnRateSharp0: float = 0.0  # float 记录riskFree=0时的资产的夏普比
        self.cashVal: float = 0.0  # float 记录持有现金
        self.secVal: float = 0.0  # float 记录持仓市值
        self.capitalReturnRate: float = 0.0  # float 记录资金的收益
        self.dateMultiDay: float = 0.0  # float 记录当前频率转换成日度频率的乘数
        self.dateMultiYear: float = 0.0  # float 记录当前频率转换成年度频率的乘数(252*self.dateMultiDay)

    def init_log(self):
        """初始化日志，注意：除非自己有特殊需求，否则不要被子类继承。"""
        self._init_log()

    def _init_log(self):
        """设置日志"""
        # 设置日志名称等于策略名
        self.logFileName: str = self.strategyName + '_' + datetime.datetime.now().strftime('%Y-%m-%d_%H,%M,%S')

        if not os.path.isdir(self.logSaveDir):
            os.mkdir(self.logSaveDir)
        path = self.logSaveDir + os.sep + self.logFileName + '.log'
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)-3d] %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', filename=path, filemode='a')

        # 定义一个StreamHandler,将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(levelname)-8s: %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    def _init_end(self):
        """其他变量设置"""

        # 设置资金总量
        self.posValSer['cash'] = self.capitalStart
        self.posValSer['val'] = self.capitalStart


        self.timeStart = \
            self.df_data[self.df_data[self.col_code] == self.df_data[self.col_code].iloc[0]][self.col_date].iloc[0]
        self.timeEnd = \
            self.df_data[self.df_data[self.col_code] == self.df_data[self.col_code].iloc[0]][self.col_date].iloc[
                -1]
        self.periodDayNum = (self.timeEnd - self.timeStart).days

        if not os.path.isdir(self.pathSaveDirName):
            os.mkdir(self.pathSaveDirName)
        self.pathPosValDF = self.pathSaveDirName + os.sep + self.strategyName + '_posValDF.csv'  # 每日交易存储路径
        self.pathTradeFlow = self.pathSaveDirName + os.sep + self.strategyName + '_tradeFlow.csv'  # 交易记录存储路径


    def get_csv_data(self, pathList):
        """
        从csv文件中获取数据源
        :param pathList: csv文件的绝对路径列表
        :return:
        """
        for path in pathList:
            code = path.split(os.sep)[-1][:-4]
            if os.path.exists(path):
                try:
                    try:
                        _df = pd.read_csv(path,  parse_dates=[0])
                    except(IOError, FileExistsError, FileNotFoundError) as err:  # IOError 是其他两个的父类，因此其他两个异常此处可以去掉。
                        logging.debug('读取文件{}触发异常{},尝试以gbk编码读取'.format(path, err))
                        _df = pd.read_csv(path,  parse_dates=[0], encoding='gbk')
                    self.secDataDict[code] = _df
                    self.secCodeList.append(code)
                except IOError as err:
                    logging.debug('读取文件{}失败，触发异常{}'.format(path, err))

        for code in self.secCodeList:
            df = self.secDataDict[code]
            df = df.rename(columns=lambda x: x.lower()) # 所有列都以小写字母表示。
            df.sort_values('date', inplace=True) # 按日期排序
#            df.reset_index(inplace=True) # 不设置date作为index，应该把date列作为column。
            df['code'] = code # 重新赋值code，确保code列非空(因为部分数据没有code列)
            self.secDataDict[code] = df
        df_data = pd.concat(self.secDataDict, ignore_index=True)
        return df_data


    def data_pre(self, df):
        """
        数据预处理函数，定义groupby('code').apply(func)中的func，需要被子类继承。
        :param df: DataFrame，单个证券的历史数据，以索引为时间
        :return:
        """
        return df

    def _on_trade(self, tim, code, num, df_now, fee=0.0, dealType='close', dealPrice=None):
        """
        实际触发交易的函数，注意参数dealPrice比dealType优先，即若设置了dealPrice，则成交价格以dealPrice为准；否则以dealType为准。若dealPrice参数为None，请注意dealType参数的有效性,若数据中不存在该列，则会报错。
        :param tim:交易的时间
        :param code:交易的代码
        :param num:成交数量
        :param df_now: 当前所有证券的行情信息
        :param fee:手续费，默认为0
        :param dealType: 设置成交的价格类型，可以是high，close，open，low等等
        :param dealPrice: 设置交易的价格，用来在某些时刻（如止损、清仓时）强制成交.
        :return:
        """
        
        '''获取bar交易记录'''
        bar = df_now.loc[code, :].copy()
        bar['fee'] = fee
        bar['num'] = num
        if dealPrice is not None:
            bar['dPrice'] = dealPrice
            bar['sum'] = dealPrice * bar['num']
        else:
            bar['dPrice'] = bar[dealType]
            bar['sum'] = bar[dealType] * bar['num']
        bar['dTime'] = str(tim)
        bar['dCode'] = code
        bar['cash'] = self.posValSer['cash']
        bar['val'] = self.posValSer['val']
        bar['secVal'] = self.posValSer['secVal']
        return bar

    def on_trade(self, tim, code, num, df_now, fee=0.0, dealType='close', dealPrice=None):
        """实际触发交易的函数，详细参数解读见self._on_trade()，需要被子类继承。"""

        bar = self._on_trade(tim, code, num, df_now, fee=fee, dealType=dealType, dealPrice=dealPrice)

        '''在子类继承中，此处可以对 bar添加其他变量。'''

        self.trade_otherSets(code, num, fee, bar)

    def on_bar(self, tim, df_now):
        """
        行情推送的主函数，在该函数中可触发on_open,on_close等等函数，需要被子类继承。
        :param tim: 日期格式，当前bar对应的时间
        :param df_now: DataFrame，当前时刻所有证券的行情数据，索引是代码。
        :return:
        """
        return

    def on_open(self, tim, df_now):
        """开仓的逻辑,该函数可触发on_trade函数进行交易，参数与self.on_bar()保持一致，需要被子类继承"""
        return

    def on_close(self, tim, df_now):
        """平仓逻辑,该函数可触发on_trade函数进行交易，参数与self.on_bar()保持一致，需要被子类继承"""
        return

    def on_clear(self, tim, df_now):
        """到期清仓逻辑，该函数可触发on_trade函数进行交易，参数与self.on_bar()保持一致，需要被子类继承"""
        return

    def run(self):
        """回溯测试的运行主体，主要过程是触发回溯测试的主函数 backtest_main,然后计算交易结果，之后进行存储与展示"""

        '''运行回溯测试主函数'''
        # print('run,df_codeIndex..........................')
        # print(self.df_codeIndex.head(1))
        self.df_codeIndex.groupby(self.col_date).apply(self.backtest_main)
        # self.df_codeIndex.groupby(self.col_date, observed=True).apply(self.backtest_main)

        # with open('df_codeIndex.pkl','wb') as file:
        #     self.df_codeIndex.to_pickle(file)

        '''计算交易回报数据'''
        self.result_calc()

        '''存储回测结果'''
        self.save_and_show()

    def init_run(self):
        """
        在回溯测试之前，进行一些设置，作用是对回溯测试进行初始化，需要被子类继承。
        """
        self._init_run()

    def _init_run(self):
        """对其他的初始化进行处理"""

        '''对df_data 常规处理'''
        self.df_data = self.df_data.rename(columns=lambda x: x.lower())  # '日线数据表头默认是大写，而高频数据默认是小写，所以需要把格式统一转换成小写才可以。'
        self.df_data = self.df_data.query('@self.start_time <= {} <= @self.end_time'.format(self.col_date))

        '''数据预处理'''
        # 把 date 数据列格式统一修改为 Timestamp
        if self.df_data.dtypes[self.col_date] != '<M8[ns]':
            self.df_data[self.col_date] = self.df_data[self.col_date].astype(np.datetime64)
        self.df_data = self.df_data.groupby(self.col_code).apply(self.data_pre)

        '''设置以code为索引的数据源'''
        self.df_codeIndex = self.df_data.set_index(self.col_code)

        '''其他变量设置,该设置依赖df_data，所以要放在后面'''
        self._init_end()

    def backtest_main(self, df_now):
        """
        回溯测试主函数，该函数会触发行情推送函数on_bar。
        原理是定义groupby('date').apply(func)中的func，作为回测主体的主函数。
        :param df_now: DataFrame，特定时刻的所有证券行情数据，索引是代码。
        :return:
        """
        # try:
        # print('>>>>>>>>>>>>backtest_main')
        # print(df_now.head(1))
        
        # 如果这里出现错误只能说明是self.on_bar函数出现了bug，而groupby又不能停下来，之后的df_now都不包含self.col_date列。
        tim = df_now[self.col_date].iloc[0]
        # try:
        #     tim = df_now[self.col_date][0]
        # except:
        #     logging.debug(r'/n出现错误/n{}'.format(df_now.head(1)))
        #     return

        # 运行行情推送函数
        self.on_bar(tim, df_now)

        logging.info(tim)

        self.workDayNum += 1
        if self.timeEndFlag in str(tim):
            '''更新用户数据'''
            self.update_posValue(tim, df_now)
            '''把PosValSer添加到PosValList里面'''
            self.posValList.append(self.posValSer.copy())
            '''初始化当前时刻的交易费用'''
            self.feeTimeList = []
        # except Exception as err:
        #     logging.debug('函数backtest_main出错了，时间{}'.format(tim))

    def get_security_value(self, tradeDict, df_now):
        """
        计算 tradeDict 内所有的股票总价值
        :param tradeDict: Dict，所选股票代码列表
        :param df_now: DataFrame，特定时刻的所有证券行情数据，索引是代码。
        :return:
        """

        money = 0
        for code, num in tradeDict.items():
            try:
                price = df_now.loc[code, self.dealType]
            except Exception as err: # KeyError Valueerror
                logging.debug('触发异常{}，获取证券 {} 持仓数量失败，当前持仓市值无效，位置：get_security_value()'.format(err, code))
                continue
            money += price * num
        return money

    def update_posValue(self, tim, df_now):
        """
        更新用户数据，参数同 on_bar
        """
        secVal = self.get_security_value(self.tradeDict, df_now)
        self.posValSer['date'] = str(tim)
        self.posValSer['secVal'] = secVal
        self.posValSer['val'] = self.posValSer['cash'] + secVal
        self.posValSer['fee'] = sum(self.feeTimeList)

    def trade_otherSets(self, code, num, fee, bar):
        """对bar添加其他信息并更新到交易列表里面"""

        '把单笔交易手续费添加到当日交易手续费序列里面去'
        self.feeTimeList.append(fee)

        '''把单个交易记录添加到交易列表里面'''
        self.tradeFlowList.append(bar)

        '''更新用户的cash'''
        self.tradeDict[code] += num
        if self.tradeDict[code] == 0:
            del self.tradeDict[code]
        self.posValSer['cash'] = self.posValSer['cash'] - bar['sum'] - fee

    def filter_tradeFlow(self):
        """过滤交易记录列表的数据信息。"""
        for col in self.colDropList:
            try:
                del self.tradeFlowDF[col]
            except KeyError as err:
                logging.debug('过滤列：{} 失败, 触发异常{}'.format(col, err))
                pass

    @staticmethod
    def sharpe_rate(ser_return, freeRiskRatio, year_multiply=242, log_flag=False):
        """
        计算夏普比的指标。
        :param ser_return: 收益率Series（根据ntim，按日、小时、保存）
        :param freeRiskRatio: 无风险收益率
        :param year_multiply: 指标转年化的乘数
        :param log_flag: 对数标记，默认不使用对数收益率
        :return:
        """

        '''如果不是对数收益率，则转化成对数收益率'''
        if  log_flag:
            ser_return = np.log(ser_return + 1)
        ser_return = ser_return.dropna()
        std = ser_return.std()
        '''如果波动率为0，说明ser_return是一个单一值，没有夏普比'''
        if std != 0:
            sharp = (ser_return.mean() - freeRiskRatio / year_multiply) / std * np.sqrt(year_multiply)
        else:
            sharp = np.nan
        return sharp

    def result_calc(self):
        """输出结果 的计算"""
        # 处理异常
        if len(self.posValList) == 0:
            logging.info('-----'*10)
            logging.info('posValList没有结果')
            return None
        '''处理posVal'''
        self.posValDF = pd.concat(self.posValList, axis=1).T
        self.posValDF['val'] = self.posValDF['val'].apply(pd.to_numeric)  # 修改val列的数据格式
        self.posValDF['date'] = self.posValDF['date'].apply(pd.to_datetime)  # 设置date列的数据格式为时间格式
        self.posValDF = self.posValDF.set_index('date')
        self.posValDF['valRate'] = self.posValDF.val.pct_change()
        self.posValDF['valCumMin'] = self.posValDF.val.cummin()
        self.posValDF['valCumMax'] = self.posValDF.val.cummax()
        #   计算最大回撤
        self.posValDF['valMaxDown'] = self.posValDF['val'] / self.posValDF['valCumMax'] - 1
        self.valMaxDown = self.posValDF['valMaxDown'].min()
        #   计算最长回撤的天数
        self.valMaxDownPeriods = self.posValDF.groupby(self.posValDF['valCumMax'])['cash'].count().max()
        #   计算回撤的最高点位
        self.valIdxMax = self.posValDF.val.idxmax()
        # todo 检查为什么会第一行会出现重复数据。
        if self.valIdxMax == self.posValDF.index[0]:
            self.valMax = self.posValDF['val'][0]
        else:
            self.valMax = self.posValDF.loc[self.valIdxMax, 'val']



        #   计算回撤的最高点位时间
        self.valIdxMaxStr = str(self.valIdxMax)
        #   计算回撤的最低点位
        self.valMin = self.posValDF['valCumMin'].min()

        '''处理其他指标'''
        self.capitalProfit = self.posValSer['val'] - self.capitalStart
        self.posValDFBus = self.posValDF.copy(deep=True)
        self.posValDFBus['day'] = self.posValDFBus.index.map(lambda x:x.date())
        self.posValDFBus.drop_duplicates(['day'], keep='last', inplace=True)
        # self.posValDFBus.set_index('day', inplace=True)
        self.posValDFBus['valRate'] = self.posValDFBus['val'].pct_change()


        # self.posValDFBus = self.posValDF.resample('B').last().ffill()  # 数据频率调整为工作日，为了避免高频运算出现错误
        # self.posValDFBus['valRate'] = self.posValDFBus['val'].pct_change()
        self.returnRateAvg = np.exp(np.log(self.posValDFBus['valRate'] + 1).mean() * 242) - 1
        self.returnRateStd = self.posValDFBus['valRate'].std() * 242 ** 0.5
        self.returnRateSharp = (self.returnRateAvg - self.riskFreeRatio ) / self.returnRateStd
        self.returnRateSharp0 = self.returnRateAvg / self.returnRateStd
        # self.returnRateSharp = self.sharpe_rate(self.posValDFBus['valRate'], freeRiskRatio=self.riskFreeRatio,
        #                                         year_multiply=252)
        # self.returnRateSharp0 = self.sharpe_rate(self.posValDFBus['valRate'], freeRiskRatio=0, year_multiply=252)
        self.cashVal = self.posValSer['cash']
        self.secVal = self.posValSer['secVal']
        self.capitalEnd = self.secVal + self.cashVal
        self.capitalReturnRate = (self.capitalEnd - self.capitalStart) / self.capitalStart
        self.dateMultiDay = self.workDayNum / (self.periodDayNum / 365 * 242)  # 计算当前频率转换成日度频率的乘数 #
        self.dateMultiYear = self.workDayNum / self.periodDayNum * 365  # 计算当前频率转换成年度频率的乘数(252*self.dateMultiDay)

    def save_and_show(self):
        """
        存储与输出交易结果
        """
        
        if len(self.tradeFlowList)==0:
            logging.info('没有产生交易结果')
            return None

        '''存储交易结果'''
        self.tradeFlowDF = pd.concat(self.tradeFlowList, axis=1).T
        self.filter_tradeFlow()
        try:
            self.tradeFlowDF.to_csv(self.pathTradeFlow, index=True, encoding='gbk')
            self.posValDF.to_csv(self.pathPosValDF, index=True, encoding='gbk')
        except IOError as err:
            logging.debug('输出tradeFlowDF或posValDF失败，触发异常{}'.format(err))
            _rnd = np.random.randn()
            pathPosValDF = self.pathPosValDF[:-4] + '_%.2f' % _rnd + '.csv'
            pathTradeFlow = self.pathTradeFlow[:-4] + '_%.2f' % _rnd + '.csv'
            self.posValDF.to_csv(pathPosValDF, index=True, encoding='gbk')
            self.tradeFlowDF.to_csv(pathTradeFlow, index=True, encoding='gbk')
            self.strategyName += '_%.2f' % _rnd

        '''输出交易结果'''
        if self.logOutput:
            logging.info('输出回溯结果' + '===' * 20)

            logging.info('交易总次数：%d', len(self.tradeFlowDF))
            logging.info('交易总盈利：%.2f', self.capitalProfit)
            logging.info("最终资产价值 Final portfolio value: $%.2f", self.capitalEnd)
            logging.info("最终现金资产价值 Final cash portfolio value: $%.2f", self.cashVal)
            logging.info("最终证券资产价值 Final stock portfolio value: $%.2f", self.secVal)
            logging.info("累计回报率 Cumulative returns: %.2f%%", (self.capitalReturnRate * 100))
            logging.info("年化收益率 Average daily return: %.3f%%", (self.returnRateAvg * 100))
            logging.info("年化波动率 Std. dev. daily return:%.4f ", self.returnRateStd)
            logging.info("年化夏普比率 Sharpe ratio: %.3f,（%.2f利率）", self.returnRateSharp, self.riskFreeRatio)
            logging.info("无风险利率 Risk Free Rate: %.2f", self.riskFreeRatio)
            logging.info("年化夏普比率 Sharpe ratio: %.3f,（0利率）", self.returnRateSharp0)
            logging.info("最大回撤率 Max. Draw Down: %.4f%%", (abs(self.valMaxDown)*100))
            logging.info("最长回撤天数 Longest Draw Down duration:% d", int(self.valMaxDownPeriods / self.dateMultiDay))
            logging.info("回撤时间(最高点位) Time High. Draw Down:{}".format(self.valIdxMaxStr))
            logging.info("回撤最高点位 High. Draw Down: %.3f", self.valMax)
            logging.info("回撤最低点位 Low. Draw Down: %.3f", self.valMin)
            logging.info("时间周期 Date lenght: %d (Day)", self.periodDayNum)
            logging.info("时间周期（交易日） Date lenght(weekday): %d (Day)", int(self.workDayNum / self.dateMultiDay))

            logging.info("开始时间 Date begin: %s", str(self.timeStart))
            logging.info("结束时间 Date lenght: %s", str(self.timeEnd))
            logging.info("策略名称 Project name: %s", self.strategyName)
            # logging.info("策略名称 Strategy name: %s" , staName)
            logging.info(
                "股票代码列表(前五) Stock list: {}".format(
                    self.secCodeList[:5] if len(self.secCodeList) > 5 else self.secCodeList))
            logging.info("策略参数  {}".format(self.strategyVarList))

        '''为绘图传递交易结果'''
        self.plotDataList.append(['交易总次数', '%d' % len(self.tradeFlowDF)])
        self.plotDataList.append(['交易总盈利', '{:,}'.format(int(self.capitalProfit))])
        self.plotDataList.append(['最终资产价值', '{:,}'.format(int(self.capitalEnd))])
        self.plotDataList.append(['最终现金资产价值', '{:,}'.format(int(self.cashVal))])
        self.plotDataList.append(['最终证券资产价值', '{:,}'.format(int(self.secVal))])
        self.plotDataList.append(['累计回报率%: ', '%.2f' % (self.capitalReturnRate * 100)])
        self.plotDataList.append(['年化收益率%: ', '%.3f' % (self.returnRateAvg * 100)])
        self.plotDataList.append(['年化波动率', '%.4f' % self.returnRateStd])
        self.plotDataList.append(['无风险利率', '%.2f' % self.riskFreeRatio])
        self.plotDataList.append(['年化夏普比率（%.2f利率）' % self.riskFreeRatio, '%.3f' % self.returnRateSharp])
        self.plotDataList.append(['年化夏普比率（无风险）', '%.3f' % self.returnRateSharp0])
        self.plotDataList.append(['最大回撤率', '%.4f' % abs(self.valMaxDown*100)])
        self.plotDataList.append(['最长回撤天数', '%d' % int(self.valMaxDownPeriods / self.dateMultiDay)])
        self.plotDataList.append(['回撤最高点位', '{:,}'.format(int(self.valMax))])
        self.plotDataList.append(['回撤最低点位', '{:,}'.format(int(self.valMin))])
        self.plotDataList.append(['时间周期（日历日）', '%d (Day)' % self.periodDayNum])
        self.plotDataList.append(['时间周期（交易日）', '%d (Day)' % int(self.workDayNum / self.dateMultiDay)])
        self.plotDataList.append(['策略参数 ', str(self.strategyVarList)])
        self.plotDataList.append(['开始时间', str(self.timeStart)])
        self.plotDataList.append(['结束时间', str(self.timeEnd)])
        self.plotDataList.append(['回撤时间(最高点位)', self.valIdxMaxStr])
        self.plotDataList.append(['策略名称', '%s' % self.strategyName])
        # plotDataList.append(['策略名称', '%s' % staName])

        '''显示绘图'''
        if self.plotMode.upper() == 'PYQT':
            self.plot_pyqt()
        elif self.plotMode.upper() == 'PLOTLY':
            self.plot_plotly()
        
        '''保存logging'''
        logging.shutdown()
        

    def plot_pyqt(self):
        """
        基于pyqt的结果输出
        :return:
        """
        from .rhPlot.rhQuant_matplotlib_show import plot_show
        plot_show(self)

    def plot_plotly(self):
        """
        基于plotly的结果输出
        :return:
        """
        from .rhPlot.rhQuant_plotly_show import plot_show
        plot_show(self)
