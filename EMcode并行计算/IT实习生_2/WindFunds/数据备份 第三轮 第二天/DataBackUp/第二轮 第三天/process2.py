# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:51:55 2020

@author: hs101
"""

'''
看看有多少种不同的股票
保存文件stocks.csv
Returns:
    股票属性[股票代码，总市值，市盈率，每股收益]
Attributes:
    每股收益：指定日前推12个月的净利润除以最新总股本计算的每股收益。
'''

import datetime
from WindPy import w
import pandas as pd
dataRaw = pd.read_csv('funds.csv',encoding = 'gbk').drop(columns = 'Unnamed: 0')


def count_time(func):
    def time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        result = func(*args, **kwargs)
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序 %s 共计%s秒' %(str(func).split(" ")[1].ljust(15,"."),total_time))
        return result
    return time


@count_time
def stocks_adding(stock_code_list):
    stocks_add = pd.DataFrame()
    for code in stock_code_list:
        stocks_add_temp = w.wsd(code, "eps_ttm,avgreturny", "2020-05-12", "2020-05-12", "returnType=1",usedf = True)[1]
        stocks_add = pd.concat([stocks_add,stocks_add_temp],sort=True).reset_index(drop=True) 
    return stocks_add

@count_time
def windProcess(stock_code_list):
    #stocks = w.wss(stock_code_list, "province,mkt_cap_CSRC,pb_lyr","unit=1;tradeDate=20200510",usedf=True)[1]
#    stocks = w.wss(stock_code_list, "ev3,pb_lyr","unit=1; tradeDate=20200510; currencyType=rmb",usedf=True)[1]

#    new_stock_code_list = stock_code_list[1:10]
#    stocks_add = stocks_adding(new_stock_code_list)
    # 省份 总市值 账面市值比 
    # 还缺一个变量 过去十二个月的收益 也就是动量
    stocks = w.wss(stock_code_list, "ev3,pb_lyr,eps_ttm","unit=1; tradeDate=20200510; currencyType=rmb",usedf=True)[1]
    return stocks


@count_time
def show_df(df): 
    def printing(string):
        print(string.ljust(73,'-'))
    def printed(string):
        print(string.ljust(73,'='))
    print()
    printed("BEGIN")
    printing("Index")
    print(df.index)
    printing("Columns")
    print(df.columns)
    printing("Head")
    print(df.head())
    printing("Tail" )
    print(df.tail())
    printed("END")
    print()

@count_time
def write_file(df,name,encoding = 'gbk'):
    df.to_csv(name, mode ='w+',encoding = 'gbk')    
    
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
    stock_code_list = lst
      
    stocks = windProcess(stock_code_list)   
    show_df(stocks)      
    write_file(stocks, "stocks.csv")

if __name__ == '__main__':
    w.start() 
    main()
#    w.stop()
