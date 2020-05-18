# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:51:55 2020

@author: hs101
"""

'''
看看有多少种不同的股票
'''

import datetime
from WindPy import w
import pandas as pd
dataRaw = pd.read_csv('funds.csv',encoding = 'gbk')
#dataRaw = pd.read_excel('WindFunds.xlsx')
#dataRaw = pd.read_csv('WindFunds.csv')
def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func()
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序共计%s秒' % total_time)
    return int_time
    
@count_time   
def main():
    fund = dataRaw
    lst = []
    count=0
    for i in range(1,11):
        count+=1
    #    print(count)
        data = fund.iloc[:,2*i+1]
        for item in data:
            if item not in lst:
                lst.append(item)    
    w.start()        
    stock_code_list = lst             
    #stocks = w.wss(stock_code_list, "province,mkt_cap_CSRC,pb_lyr","unit=1;tradeDate=20200510",usedf=True)[1]
    stocks = w.wss(stock_code_list, "ev3,pb_lyr","unit=1;tradeDate=20200510;currencyType=rmb",usedf=True)[1]
    # 省份 总市值 账面市值比 
    # 还缺一个变量 过去十二个月的收益 也就是动量
    w.stop()
    stocks.to_csv("stocks.csv", mode ='w+',encoding = 'gbk')


if __name__ == '__main__':
    main()
