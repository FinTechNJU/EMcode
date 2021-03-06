# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:18:38 2020

@author: hs101
"""
'''
Purpose:
    获得股票和基金的属性，生成初始化指标
Dependency:
    ./process2.py
Returns:
    K:   有多少个城市，这里用省份代替
    N:   有多少个基金经理
    J_k: 一个股票有多少个权重，这里所有的J_k都是同一个值

Results:
    K:   31个城市
    N:   259个基金经理
    J_k: 10个权重 
    
'''
from process2 import show_dfs
import pandas as pd
dataRaw1 = pd.read_csv("stocks.csv",encoding = 'gbk')
dataRaw2 = pd.read_csv("funds.csv",encoding = 'gbk').drop(["Unnamed: 0"],axis =1)
dataRaw3 = pd.read_csv('cities.csv',encoding = 'gbk').drop(["Unnamed: 0"],axis =1)
dataRaw4 = pd.read_csv("managers.csv", encoding = 'gbk').drop(['0'],axis =1)
dataRaw5 = pd.read_csv('stock_province.csv', encoding = 'gbk').drop(['EV3', 'PB_LYR', 'EPS_TTM'], axis =1)

def fund2fundCity(fund, stock_province):
    fundCity = fund
    for i in range(fund.shape[0]):
        for j in range(10):
            code = fundCity.iat[i, 2*j+3]
            for k in range(stock_province.shape[0]):
                if stock_province.iat[k, 0] == code:
                    fundCity.iat[i, 2*j+3] = stock_province.iat[k, 1]
                    break
    return fundCity


if __name__ == "__main__":
    fund = dataRaw2
    stock = dataRaw1
    city = dataRaw3
    manager = dataRaw4
    stock_province = dataRaw5
    show_dfs([fund, stock, city, manager])
    K = city.shape[0]
    J_k = 10
    N = manager.shape[0]
    info_dict = {}
    info_dict['K'] = K
    info_dict["N"] = N
    info_dict['J_k'] = J_k
    print(info_dict)
    
    fundCity = fund2fundCity(fund, stock_province)
    fundCity.to_csv('fundCity.csv', mode = 'w+', encoding = 'gbk')