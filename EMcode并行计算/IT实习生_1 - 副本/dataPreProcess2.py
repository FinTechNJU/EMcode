# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:28:25 2020

@author: hs101
"""

import pandas as pd
fundsRaw = pd.read_csv("funds.csv",encoding = 'gbk').drop('Unnamed: 0',axis =1)

fund = fundsRaw
lst = []
for i in range(1,11):
    data = fund.iloc[:,2*i]
    for item in data:
        if item not in lst:
            lst.append(item)

from WindPy import w
w.start()

def exchange(x):
    if(x[-1] == 'G'):
        return '.SH'
    elif(x[-1] == 'E'):
        return '.SZ'
    
stock_code_list = []   
for i in range(len(lst)):
    code = lst[i][1:-1]
    stock_code = code[:-5] + exchange(code)
    stock_code_list.append(stock_code)
    
stocks = w.wss(stock_code_list, "province,mkt_cap_CSRC,pb_lyr","unit=1;tradeDate=20200510",usedf=True)[1]
# 省份 总市值 账面市值比 
# 还缺一个变量 过去十二个月的收益 也就是动量
w.stop()

stocks.to_csv("stocks.csv", mode ='w+', encoding = 'gbk')
