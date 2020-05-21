# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:18:04 2020

@author: hs101
"""

import pandas as pd


maxReduce = pd.read_csv("maxReduce.csv", encoding = 'gbk')
funds = pd.read_csv('funds.csv', encoding = 'gbk')
managers = pd.read_csv('managers.csv', encoding = 'gbk')
stock_province = pd.read_csv('stock_province.csv', encoding = 'gbk')

index_list = []
for i in range(funds.shape[0]):
    if funds.iloc[i,3] in list(managers.iloc[:,1]):
        index_list.append(i)
        
new_fund = funds.iloc[index_list,:]
new_fund.to_csv("new_fund.csv", mode ='w+', encoding = 'gbk')

fund_list = new_fund.iloc[:,1]

index_list2 = []
for i in range(maxReduce.shape[0]):
    if maxReduce.iloc[i,1] in list(fund_list):
        index_list2.append(i)
new_maxReduce = maxReduce.iloc[index_list2,:]
new_maxReduce = new_maxReduce[new_maxReduce['maxReduceShare']<=-100]


new_maxReduce.to_csv("new_maxReduce.csv", mode ='w+', encoding = 'gbk')

new_manager = new_maxReduce.iloc[:,3]
new_manager = pd.Series(list(set(new_manager)))
new_manager.to_csv("new_manager.csv", mode ='w+', encoding = 'gbk')

new_stock = list(set(new_maxReduce.iloc[:,4]))
new_stock = pd.Series(new_stock)
new_stock.to_csv("new_stock.csv", mode ='w+', encoding = 'gbk')

index_list3 = []
for i in range(stock_province.shape[0]):
    if stock_province.iloc[i,0] in list(new_stock):
        index_list3.append(i)
new_province =  list(set(stock_province.iloc[index_list3,1]))
new_province = pd.Series(new_province)
new_province.to_csv('new_province.csv',encoding = 'gbk',mode = 'w+')