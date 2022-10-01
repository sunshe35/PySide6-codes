from quant.rhQuant import *
import copy
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 150)


class StrategyDemo(RhQuant):
    """
    RhQuant 实例化类
    """

    def __init__(self):
        super().__init__()
        '''necessary, 以下变量必须重写'''
        # self.start_time = '2017-01-01'  # str 回测的初试时间
        self.start_time = '2014-09-01'  # str 回测的初试时间
        self.end_time = '2017-09-1'  # str 回测的初试时间
        # self.end_time = '2021-01-23'  # str 回测的终止时间
        self.capitalStart = 1e6  # 初始化资金量
        self.strategyName = '下影线策略'  # 策略名称
        # self.timeEndFlag = '15:00:00'  # 记录高频数据每天最后一个交易时刻的标记，若数据为日度数据，可设置为：''
        self.timeEndFlag = ''  # 记录高频数据每天最后一个交易时刻的标记，若数据为日度数据，可设置为：''

        '''options, 以下变量可以根据实际情况进行重写'''
        self.plotMode = 'pyqt'  # 支持plotly与pyqt两种输出模式。
        # self.plotMode = 'plotly'  # 支持plotly与pyqt两种输出模式。

        # self.code_tup = ('000001.XSHG',"000016.XSHG")
        self.code_tup = ("000001.XSHG",)  # 000016.XSHG 上证50
        self.colDropList: list = ['high', 'low', 'open', 'day_t', 'pubdate_t', 'net_profit_t']  # 设置在tradeFlow中要删除的一些列表

        '''custom, 以下变量为策略自定义的变量'''
        # self.strategyName = self.strategyName + self.base_code

    def init_data(self):
        df = pd.read_csv(r'data/TF.CFE_15.csv')
        df['code'] = 'TF.CFE'
        self.df_data = df

    def data_pre(self, df):
        """
        数据预处理函数，定义groupby('code').apply(func)中的func，需要被子类继承。
        :param df: DataFrame，单个证券的历史数据，以索引为时间
        :return:
        """
        df['close'] = df['close'].fillna(method='ffill')  # 前向填充价格与成交量，因为高频数据有些时刻数据是空值
        df['volume'] = df['volume'].fillna(method='ffill')
        df['volume_avg'] = df['volume'].rolling(5).mean()
        df['trade_flag'] = np.where(df['volume'] > 2 * df['volume_avg'], 1, 0)

        OC_max = df.loc[:, ['close', 'open']].max(1)
        OC_min = df.loc[:, ['close', 'open']].min(1)
        ser_low_shadow = np.where(OC_min - df['low'] > 0.1, 1, 0)
        ser_high_shadow = np.where(df['high'] - OC_max > 0.1, -1, 0)
        df['shadow_sum'] = ser_high_shadow + ser_low_shadow
        return df

    def init_run(self):
        """
        在回溯测试之前，进行一些设置，需要被子类继承。
        :return:
        """
        self._init_run()
        self.df_codeIndex.dropna(axis='index', how='any', subset=['open', 'volume'], inplace=True)  # 剔除已经停止上市的合约

    def on_trade(self, tim, code, num, df_now, fee=0.0, dealType='close', dealPrice=None):
        """
        实际触发交易的函数，注意参数dealPrice比dealType优先，即若设置了dealPrice，则成交价格以dealPrice为准；否则以dealType为准。若dealPrice参数为None，请注意dealType参数的有效性,若数据中不存在该列，则会报错。
        :param tim:交易的时间
        :param code:交易的代码
        :param num:成交数量
        :param df_now: 当前所有证券的行情信息
        :param fee:手续费，默认为0.0
        :param dealType: 设置成交的价格类型，可以是high，close，open，low等等
        :param dealPrice: 设置交易的价格，用来在某些时刻（如止损、清仓时）强制成交.
        :return:
        """

        '''num数量为0则不触发交易'''
        if num == 0:
            logging.debug('代码：{}，时间：{}，成交量为0'.format(code, tim))
            return None

        bar = self._on_trade(tim, code, num, df_now, fee=fee, dealType=dealType, dealPrice=dealPrice)
        bar['margin_ratio'] = self.marginRatio
        for each in ['open_num', 'trade_way', 'pos_num', ]:
            bar[each] = self.posDict[each]
        self.trade_otherSets(code, num, fee, bar)

    def on_bar(self, tim, df_now):
        """
        行情推送的主函数，在该函数中可触发on_open,on_close等等函数，需要被子类继承。
        :param tim: 日期格式，当前bar对应的时间
        :param df_now: DataFrame，当前时刻所有证券的行情数据，索引是代码。
        :return:
        """

        '''检测清仓'''
        # if str(tim).split(' ')[-1] == '15:15:00':
        if tim.strftime('%H-%M') == '15:15':
            print(tim)
            '''检测并处理清仓信息'''
            self.on_clear(tim, df_now)
        else:
            '''检测平仓'''
            self.on_close(tim, df_now)

            '''检测开仓'''
            self.on_open(tim, df_now)

    def on_clear(self, tim, df_now):
        """清仓逻辑,该函数可触发on_trade函数进行交易，参数与self.on_bar()保持一致，需要被子类继承"""

        _posFullDict = copy.deepcopy(self.posFullDict)
        # df = df_now.copy()
        for open_num in _posFullDict:
            self.posDict = _posFullDict[open_num]
            trade_stock = self.posDict['stock']
            code = self.posDict['code']

            '''触发平仓信号'''
            del self.posFullDict[open_num]  # 删除组合持仓记录
            self.countClear += 1
            logging.info('平<---,开:{}-平:{}-清:{}'.format(self.countOpen, self.countClose, self.countClear))
            for code in trade_stock:
                trade_volume = trade_stock[code]
                self.posDict['trade_way'] = '清'
                self.on_trade(tim, code, trade_volume * -1, df_now, dealType='close')
                logging.info('清仓<---{}'.format(code))

    def on_close(self, tim, df_now):
        """平仓逻辑,该函数可触发on_trade函数进行交易，参数与self.on_bar()保持一致，需要被子类继承"""
        _posFullDict = copy.deepcopy(self.posFullDict)
        # df = df_now.copy()
        for open_num in _posFullDict:
            self.posDict = _posFullDict[open_num]
            trade_stock = self.posDict['stock']
            trade_way = self.posDict['trade_way']

            # 开仓当天不可以平仓。
            trade_time = self.posDict['trade_time']
            if trade_time.date() == tim.date():
                return None

            left_day = self.posDict['left_day']

            if left_day == 0:
                '''触发平仓信号'''
                del self.posFullDict[open_num]  # 删除组合持仓记录
                self.countClose += 1
                logging.info('平<---,开:{}-平:{}-清:{}'.format(self.countOpen, self.countClose, self.countClear))
                for code in trade_stock:
                    trade_volume = trade_stock[code]
                    self.posDict['trade_way'] = '多平' if trade_way == '多开' else '空平'
                    self.on_trade(tim, code, trade_volume * -1, df_now, dealType='close')
                    logging.info('平仓<---{}'.format(code))
            else:
                self.posFullDict[open_num]['left_day'] -= 1

    def on_open(self, tim, df_now):
        """
        开仓的逻辑,该函数可触发on_trade函数进行交易，参数与self.on_bar()保持一致，需要被子类继承
        """
        # 只允许一次开仓。
        if len(self.posFullDict) > 0:
            return

        code = df_now.index[0]
        close = df_now.at[code, 'close']

        trade_flag = df_now.at[code, 'trade_flag']
        shadow_sum = df_now.at[code, 'shadow_sum']
        if trade_flag == 1 and shadow_sum != 0:
            cash = self.posValSer['cash']
            if shadow_sum > 0:
                trade_volume = 5 * self.contractUnit * 1
            else:
                trade_volume = 5 * self.contractUnit * -1
            '''记录这次交易信息的组合信息'''
            self.posDict = {}
            self.posDict['stock'] = {code: trade_volume}
            self.posDict['trade_time'] = tim
            # self.posDict['macd'] = macd
            self.posDict['open_num'] = self.countOpen
            self.posDict['pos_num'] = len(self.posFullDict) + 1
            self.posDict['trade_day'] = tim.strftime('%Y-%m-%d')
            self.posDict['trade_way'] = '多开'
            self.posDict['code'] = code
            self.posDict['trade_price'] = close
            self.posDict['loss_price'] = close
            self.posDict['left_day'] = 2
            self.posDict['contractUnit'] = self.contractUnit
            self.posFullDict[self.countOpen] = self.posDict  # 增加持有信息。

            self.countOpen += 1
            logging.info('开<---,开:{}-平:{}-清:{}'.format(self.countOpen, self.countClose, self.countClear))

            fee = 5 * 4 * 2
            self.on_trade(tim, code, trade_volume, df_now, fee=fee, dealType='close')
            logging.info('开仓<---{}'.format(code))


if __name__ == '__main__':
    '''运行回溯测试'''
    qt = StrategyDemo()  # 初始化参数
    qt.init_log()  # 初始化日志
    qt.init_data()  # 初始化数据
    qt.init_run()  # 回溯测试之前的处理
    qt.run()  # 回溯测试

