# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:51:55 2020

@author: hs101
"""

import pandas as pd
dataRaw = pd.read_excel('WindFunds.xlsx')
#dataRaw = pd.read_csv('WindFunds.csv')

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

from WindPy import w
w.start()


stock_code_list = lst 

    
#stocks = w.wss(stock_code_list, "province,mkt_cap_CSRC,pb_lyr","unit=1;tradeDate=20200510",usedf=True)[1]
stocks = w.wss(stock_code_list, "ev3,pb_lyr","unit=1;tradeDate=20200510;currencyType=rmb",usedf=True)[1]
# 省份 总市值 账面市值比 
# 还缺一个变量 过去十二个月的收益 也就是动量
w.stop()

stocks.to_csv("stocks.csv", mode ='w+')
