# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:46:41 2020

@author: hs101
"""
import re
import pandas as pd
newManager = pd.read_csv('newManager.csv',encoding = 'gbk')
newProvince = pd.read_csv('newProvince.csv',encoding = 'gbk')
portweight = pd.read_csv('portweight.csv',encoding = 'gbk').drop(['Unnamed: 0'], axis = 1)
stockchara = pd.read_csv('stockchara.csv',encoding = 'gbk').drop(['Unnamed: 0'], axis = 1)
province = pd.read_csv('./old_data/cities.csv', encoding = 'gbk')

def check_1(portweight, stockchara):
    for i in range(stockchara.shape[0]):
#        if i == 1:
#            print("test")
#        print(i)
        list1 = re.split(r',\s|;\s',stockchara.iloc[i,0])
        list2 = re.split(r',\s',portweight.iloc[0,i])
        length1 = len(list1)
        length2 = len(list2)
        assert length1 == 3 * length2

def delete_manager(portweight, newProvince, newManager):
    portweight.set_index(['manager'], inplace = True)
    list1 = list(newManager.iloc[:,2])
    temp1 = portweight.loc[list1,:]
    list2 = list(newProvince.iloc[:,2])
    temp2 = temp1.loc[:,list2]  
    portweight = temp2
    return portweight

def delete_province(stockchara, newProvince):
    stockchara.set_index(['province'], inplace = True)
    list1 = list(newProvince.iloc[:,2])
    stockchara = stockchara.loc[list1,:]
    for i in range(stockchara.shape[0]):
        stockchara.iat[i,0] = stockchara.iat[i,0][1:-1]
    return stockchara
    

portweight = delete_manager(portweight, newProvince, newManager)
portweight.to_csv("./cleaned/portweightRaw.csv", mode ='w+', encoding = 'gbk')

stockchara = delete_province(stockchara, newProvince)
check_1(portweight, stockchara)
stockchara.to_csv("./cleaned/stockcharaRaw.csv", mode ='w+', encoding = 'gbk')


