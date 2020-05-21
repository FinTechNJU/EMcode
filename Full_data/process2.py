# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:11:27 2020

@author: hs101
"""


import pandas as pd


def get_dataRaw_WindFunds_data():
    citiesRaw = pd.read_csv('./WindFunds_data/cities.csv',encoding='gbk').drop(['Unnamed: 0'], axis = 1)
    fundsRaw = pd.read_csv('./WindFunds_data/funds.csv',encoding='gbk').drop(['Unnamed: 0'], axis = 1)    
    fundsRaw = fundsRaw.set_index(['证券代码'])
    stocksRaw = pd.read_csv('./WindFunds_data/stocks.csv',encoding='gbk').set_index(['Unnamed: 0'])
    fundCityRaw = pd.read_csv('./WindFunds_data/fundCity.csv',encoding='gbk').drop(['Unnamed: 0'], axis = 1)
    fundCityRaw = fundCityRaw.set_index(['证券代码'])
    stock_province = pd.read_csv('./WindFunds_data/stock_province.csv',encoding='gbk')
    stock_provinceRaw = pd.DataFrame()  
    stock_provinceRaw['city'] = stock_province.iloc[:,1]
    stock_provinceRaw.index = stock_province.iloc[:,0]     
    return citiesRaw, fundsRaw, stocksRaw, fundCityRaw, stock_provinceRaw

def get_dataRaw_WindStocks_data():
    path = './WindStocks_data/matlab_set_up/'
    cities_new = pd.read_csv(path+'newProvince.csv',encoding='gbk').drop(['0', 'Unnamed: 0'],axis=1)
    managers_new = pd.read_csv(path+'newManager.csv',encoding='gbk').drop(['0', 'Unnamed: 0'],axis=1)
    stocks_new = pd.read_csv(path+'newStock.csv',encoding='gbk').drop(['0', 'Unnamed: 0'],axis=1)
    return cities_new, stocks_new, managers_new
    

cities, funds, stocks, fundcity, stockcity = get_dataRaw_WindFunds_data()
# 获得信息：城市 基金 股票性质 股票城市

cities_new, stocks_new, managers_new = get_dataRaw_WindStocks_data()
# 获得新的 经理人 股票 和 城市




# ============================================================================ #


reducePer= pd.read_csv('./基金总净值和股价减持占比_output/减持百分比.csv',encoding='gbk').set_index('fundCode')
preserve=reducePer.iloc[:,[-2,-1]]
funds = preserve.join(funds,how='inner').drop(['fundTotalValue','percent'],axis=1)
fundcity = preserve.join(fundcity,how='inner').drop(['fundTotalValue','percent'],axis=1)
manager = reducePer.manager
manager_this = manager


# ============================================================================ #


#list1 = list(funds.iloc[:,1] )
#list2 = list(manager_this.iloc[:,0])
#index_list=[]
#for i in range(funds.shape[0]):
#    if list1[i] in list2:
#        index_list.append(i)
#funds = funds.iloc[index_list,:]
#fundcity = fundcity.iloc[index_list,:]
## 获得实验要用到的funds 和fundcity

stock_code_list = []
for i in range(funds.shape[0]):
    line = funds.iloc[i,:]
    for j in range(10):
        stock_code=line[2*j+2]
        if stock_code not in stock_code_list:
            stock_code_list.append(stock_code)
# 获得实验要用到的股票代码

province_list = []
for i in range(len(stock_code_list)):
    stock = stock_code_list[i]
    province_list.append(stockcity.loc[stock].values.tolist()[0])
province_list = list(set(province_list))
# 获得实验要用到的省份列表
    
province_stock_dict = {}
for i in range(len(province_list)):
    province_stock_dict[province_list[i]] = []
# 得出空的字典
for i in range(len(stock_code_list)):
    stock = stock_code_list[i]
    key = stockcity.loc[stock].values.tolist()[0]
    province_stock_dict[key].append(stock)
# 获得实验要用到的省份股票字典
    
    
    
    
    
# ============================================================================ #

pw = pd.DataFrame()
for i in range(len(province_list)):
    pw[province_list[i]] = [[] for i in range(len(manager_this))]
pw['manager'] = manager_this.values.tolist()
pw = pw.set_index('manager')    
# 获得portweight的基本框架
  
for i in range(pw.shape[0]):
    line = funds.iloc[i,:]
    code_dict={}
    for j in range(10):
        key = line[2*j+2]
        value = line[2*j+3]
        code_dict[key]=value
    # 获得一行 也就是一个基金经理的股权：权重
    for j in range(pw.shape[1]):
        province = pw.columns.values.tolist()[j]
        stock_list = province_stock_dict.get(province)
        result = [0.00 for i in range(len(stock_list))]
        for key,value in code_dict.items():
            province_get = stockcity.loc[key].values.tolist()[0]
            if province_get == province:
                for k in range(len(stock_list)):
                    if key == stock_list[k]:
                        result[k] = value
        pw.iat[i,j] = result
# 获得portweight\
pw.to_csv('./5_20/portweightRaw.csv',encoding='gbk',mode='w+')



# ============================================================================ #










































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    