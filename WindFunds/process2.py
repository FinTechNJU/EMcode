# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:51:55 2020

@author: hs101
"""

'''
Purpose:
    看看有多少种不同的股票
    保存文件stocks.csv
    统计有多少不同的城市
Returns:
    股票属性[股票代码，总市值，市盈率，每股收益]
Attributes:
    每股收益：
        Profile:
            指定日前推12个月的净利润除以最新总股本计算的每股收益。
        Algorithm:
            归属母公司股东的净利润(TTM)／最新总股本
            注：归属母公司净利润(TTM)为按照正式定期报告数据计算的TTM数据，最新业绩快报参与计算。
'''

import numpy as np
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
    def special_case(stocks):
        '''600031.sh的值得不到，我们用平均值来代替
        '''
        code_list = ["600031.SH", '000425.SZ']
        for item in code_list:           
            stocks.loc[item].PB_LYR = stocks.PB_LYR.mean()
        return stocks
    def calculate(stocks):
        '''对市值取log
        '''
        stocks.EV3 = np.log(stocks.EV3)
        return stocks
    #stocks = w.wss(stock_code_list, "province,mkt_cap_CSRC,pb_lyr","unit=1;tradeDate=20200510",usedf=True)[1]
#    stocks = w.wss(stock_code_list, "ev3,pb_lyr","unit=1; tradeDate=20200510; currencyType=rmb",usedf=True)[1]

#    new_stock_code_list = stock_code_list[1:10]
#    stocks_add = stocks_adding(new_stock_code_list)
    # 省份 总市值 账面市值比 
    # 还缺一个变量 过去十二个月的收益 也就是动量
    stocks = w.wss(stock_code_list, "ev3,pb_lyr,eps_ttm","unit=1; tradeDate=20200510; currencyType=rmb",usedf=True)[1]
    stocks = special_case(stocks)
    stocks = calculate(stocks)
    return stocks

def show_df(df): 
    def printing(string):
        print(string.ljust(73,'-'))
    def printed(string,symbol = "="):
        print(string.ljust(73,symbol))
    printed("BEGIN","=")
    printing("Index")
    print(df.index)
    printing("Columns")
    print(df.columns)
    printing("Head")
    print(df.head())
    printing("Tail" )
    print(df.tail())
    printed("END","=")
    print()
    print()

@count_time
def show_dfs(df_list):
    for i in range(len(df_list)):
        print()
        print(("这是第 %d 个DataFrame"%(i+1)).ljust(70,'='))
        show_df(df_list[i])

@count_time
def write_file(df,name):
    df.to_csv(name, mode ='w+',encoding = 'gbk') 

def nothing_valueable(citi_df):
    '''海南省只有一家公司
    '''
    citi_dict = {}
    for i in range(citi_df.shape[0]):
        item = citi_df.iloc[i,0]
        citi_dict[item] = citi_dict.get(item,0) +1
    for i in range(citi_df.shape[0]):
        item = citi_df.iloc[i,0]
        if item == "海南省":
            break
    return i, citi_dict
    
@count_time  
def windCitiCounts(stock_code_list):
    def special_case(df):
        '''
        0005.HK设置总部在"香港特别行政区"
        1521.HK设置总部在"香港特别行政区"
        1928.HK设置总部在"香港特别行政区"
        0291.HK设置总部在"香港特别行政区"
        '''
        province = "香港特别行政区"
        code_list = ['0005.HK', '1521.HK', '1928.HK', '0291.HK']
        for i in range(len(code_list)):
            df.loc[code_list[i]] = province
        return df
    citi_list = []
    citi_df = w.wss(stock_code_list, "province","unit=1; tradeDate=20200510; currencyType=rmb",usedf=True)[1]
    citi_df = special_case(citi_df)
    for i in range(citi_df.shape[0]):
        item = citi_df.iloc[i,0]
        if item not in citi_list:
            citi_list.append(item)
    return citi_list
    



if __name__ == '__main__':
    w.start() 
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
    
    citi_list = windCitiCounts(stock_code_list)
    citi_df = pd.DataFrame(citi_list)
    show_df(citi_df)
    citi_df.to_csv("cities.csv", mode = 'w+',encoding = 'gbk')
#    w.stop()
