'''
模拟巨潮资讯的网络爬虫。
'''

import requests


def get_one_page_data(key, date_start='', date_end='', fulltext_str_flag='false', page_num=1, pageSize=30,sortName='nothing',sortType='desc'):
    '''
    :param key: 搜索的关键字
    :param date_start:起始时间 
    :param date_end: 终止时间
    :param fulltext_str_flag:是否是内容搜索，默认false，即标题搜索 
    :param page_num: 要搜索的页码
    :param pageSize: 每页显示的数量
    :param sortName: 排序名称，对应关系为：'相关度': 'nothing', '时间': 'pubdate', '代码': 'stockcode_cat'，默认为相关度
    :param sortType: 排序类型，对应关系为：'升序': 'asc', '降序': 'desc'，默认为降序
    :return: 总页码 和 当前页码的信息。
    '''
    params = {'searchkey': key,
              'sdate': date_start,
              'edate': date_end,
              'isfulltext': fulltext_str_flag,
              'sortName': sortName,
              'sortType': sortType,
              'pageNum': str(page_num),
              'pageSize': str(pageSize)}
    key_encode = requests.models.urlencode({'a': key}).split('=')[1]

    url = 'http://www.cninfo.com.cn/new/fulltextSearch/full'
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
               'Connection': 'keep-alive',
               'Cookie': "JSESSIONID=23E2CC3023E06C05019FD45FE1BFFFFE; insert_cookie=37836164; routeId=.uc2; _sp_ses.2141=*; SID=57e23463-a251-4611-a9ca-a852461cedff; cninfo_user_browse=688981,gshk0000981,%s; _sp_id.2141=85f1158d-08ae-4474-9644-377d28341141.1610205512.2.1610253491.1610205652.de893c50-a907-4359-b834-904524a6a37f"%key_encode,
               'Host': 'www.cninfo.com.cn',
               'Referer': 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=%s' % key_encode,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=20)
        # r.encoding = 'utf-8'
        page_content = r.json()
        page_value = page_content['announcements']
        total_page_num = page_content['totalpages']
        if total_page_num==0:
            return 0,[]
        else:
            return total_page_num, page_value
    except:
        return None, []


if __name__ == '__main__':
    total_num, page_value = get_one_page_data('中国中车', date_start='2015-01-05', date_end='2015-07-03')
    print(total_num, page_value)
