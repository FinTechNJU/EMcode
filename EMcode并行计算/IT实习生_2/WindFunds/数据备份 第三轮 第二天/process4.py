# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:47:42 2020

@author: hs101
"""
'''
Purpose:
    获得portweight.csv
Dependency:
    None
'''


import pandas as pd
dataRaw1 = pd.read_csv("stocks.csv",encoding = 'gbk')
dataRaw2 = pd.read_csv("funds.csv",encoding = 'gbk').drop(["Unnamed: 0"],axis =1)
dataRaw3 = pd.read_csv('cities.csv',encoding = 'gbk').drop(["Unnamed: 0"],axis =1)
dataRaw4 = pd.read_csv("managers.csv", encoding = 'gbk').drop(['Unnamed: 0'],axis =1)
dataRaw5 = pd.read_csv('stock_province.csv', encoding = 'gbk').drop(['EV3', 'PB_LYR', 'EPS_TTM'], axis =1)
dataRaw6 = pd.read_csv("fundCity.csv",encoding = 'gbk').drop(["Unnamed: 0"],axis =1)


def portweight(fundCity, city):
    pw = pd.DataFrame()
    pw['manager'] = fundCity.iloc[:,2]
    for i in range(city.shape[0]):
        province = city.iloc[i,0]
        pw[province] = pd.Series(pd.Series([[] for i in range(fundCity.shape[0])]))
    assert pw.shape == (259, 32)
    for i in range(fundCity.shape[0]):
        line = fundCity.iloc[i,:]
        wgtDict = {}
        for j in range(10):
            key = line[2*j+3]
            value = line[2*j+4]
            dict_value = wgtDict.get(key,[])
            dict_value.append(value)
            wgtDict[key] = dict_value
#        print(wgtDict)
        # 生成字典是没问题的
        
        
        for j in range(0,31):
            province =city.iloc[j,0]
            pw.iat[i,j+1] = wgtDict.get(province, 0)
    return pw



if __name__ == "__main__":
    fund = dataRaw2
    stock = dataRaw1
    city = dataRaw3
    manager = dataRaw4
    stock_province = dataRaw5
    fundCity = dataRaw6
    
    pw = portweight(fundCity, city)
    pw.to_csv('portweight.csv',mode = 'w+', encoding = 'gbk')
