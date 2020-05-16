# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:13:54 2020

@author: hs101
"""

import pandas as pd

new_maxReduce = pd.read_csv("new_maxReduce.csv", encoding = 'gbk' ).drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1)
new_manager = pd.read_csv("new_manager.csv", encoding = 'gbk',header = None)
new_province = pd.read_csv("new_province.csv", encoding = 'gbk' ,header = None)
new_stock = pd.read_csv("new_stock.csv", encoding = 'gbk',header = None)  

index_dict = {}
for i in range(new_maxReduce.shape[0]):
    key = new_maxReduce.iloc[i,3]
    value = index_dict.get(key,[])
    value.append(i)
    index_dict[key] = value
    
index_list = []
for value in index_dict.values():
    index_list.append(value[0])

newManager = new_manager.iloc[index_list,:]
newMaxReduce = new_maxReduce.iloc[index_list,:]
newStock = new_stock
newProvince = new_province
#newProvince = new_province.iloc[index_list,:]
#newStock = new_stock.iloc[index_list,:]
newManager.to_csv("./matlab_set_up/newManager.csv", mode ='w+', encoding = 'gbk')
newMaxReduce.to_csv("./matlab_set_up/newMaxReduce.csv", mode ='w+', encoding = 'gbk')
newStock.to_csv("./matlab_set_up/newStock.csv", mode ='w+', encoding = 'gbk')
newProvince.to_csv("./matlab_set_up/newProvince.csv", mode ='w+', encoding = 'gbk')
