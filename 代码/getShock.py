# 用于拉取股票历史数据

import pandas as pd
import akshare as ak

def get(stock_code):
    # 参数调整
    start_date = '20190101'
    end_date = '20210101'
    period = 'daily'
    adj = 'hfq'

    # 获取数据

    data = ak.stock_zh_a_hist(symbol=stock_code,period = period, start_date=start_date, end_date=end_date, adjust = adj)

    data.to_csv('D:\\'+ stock_code + '.csv',index = False, mode = 'w', encoding = 'gbk')

    print("-------- Get Data Done -------")