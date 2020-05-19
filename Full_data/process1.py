# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:55:07 2020

@author: hs101
"""
import numpy as np
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

manager_this = managers_new
#manager_this.to_csv('./Smaller_data_data/manaers_this.csv',encoding='gbk',mode='w+')
# 第一下 本实验要用到的经理人


list1 = list(funds.iloc[:,1] )
list2 = list(manager_this.iloc[:,0])
index_list=[]
for i in range(funds.shape[0]):
    if list1[i] in list2:
        index_list.append(i)
funds = funds.iloc[index_list,:]
fundcity = fundcity.iloc[index_list,:]
# 获得实验要用到的funds 和fundcity

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

delete_stock_code =[]
for value in province_stock_dict.values():
    if len(value) == 1:
        delete_stock_code.append(value[0])
#delete_stock_code=['000661.SZ', '000703.SZ', '600809.SH', '002185.SZ']
# 要去掉的几个股票
delete_funds_list=[]
for i in range(funds.shape[0]):
    line = funds.iloc[i,:]
    line_stock_list = []
    for j in range(10):
        stock_code=line[2*j+2]
        line_stock_list.append(stock_code)
    for k in range(len(delete_stock_code)):
        if delete_stock_code[k] in line_stock_list:
            delete_funds_list.append(i)
# 得到要删掉的行的行号
number = [i for i  in range(funds.shape[0])]
number = list(set(number).difference(set(delete_funds_list)))
funds_this = funds.iloc[number,:]
# 获得实验要用到的基金

manager_this = []
for i in range(funds_this.shape[0]):
    manager = funds_this.iat[i,1]
    manager_this.append(manager)
# 获得实验要用到的经理人    
    
stock_this = []
for i in range(funds_this.shape[0]):
    line = funds_this.iloc[i,:]
    for j in range(10):
        stock_code = line[2*j+2]
        stock_this.append(stock_code)
stock_this = list(set(stock_this))   
# 获得实验要用到的股票代码


province_list_this = []
for i in range(len(stock_this)):
    stock = stock_this[i]
    province_list_this.append(stockcity.loc[stock].values.tolist()[0])
province_list_this = list(set(province_list_this))
# 获得实验要用到的省份列表

province_stock_dict_this = {}
for i in range(len(province_list_this)):
    province_stock_dict_this[province_list_this[i]] = []
# 得出空的字典
for i in range(len(stock_this)):
    stock = stock_this[i]
    key = stockcity.loc[stock].values.tolist()[0]
    province_stock_dict_this[key].append(stock)
# 获得实验要用到的省份股票字典

# ================================================= #

pw = pd.DataFrame()
for i in range(len(province_list_this)):
    pw[province_list_this[i]] = [[] for i in range(len(manager_this))]
pw['manager'] = manager_this
pw = pw.set_index('manager')    
# 获得portweight的基本框架
  
for i in range(pw.shape[0]):
    line = funds_this.iloc[i,:]
    code_dict={}
    for j in range(10):
        key = line[2*j+2]
        value = line[2*j+3]
        code_dict[key]=value
    # 获得一行 也就是一个基金经理的股权：权重
    for j in range(pw.shape[1]):
        province = pw.columns.values.tolist()[j]
        stock_list = province_stock_dict_this.get(province)
        result = [0.00 for i in range(len(stock_list))]
        for key,value in code_dict.items():
            province_get = stockcity.loc[key].values.tolist()[0]
            if province_get == province:
                for k in range(len(stock_list)):
                    if key == stock_list[k]:
                        result[k] = value
        pw.iat[i,j] = result
# 获得portweight\
pw.to_csv('./output/portweightRaw.csv',encoding='gbk',mode='w+')
# ============================================================================ #

#sc = pd.DataFrame()
#sc['info']= [[] for i in range(pw.shape[1])]
#sc['city'] = province_list_this
#sc = sc.set_index('city')                     
## 获得stockchara的基本框架


def get_stc_prvc_dict(stock_province):
    stc_prvc_dict = {}
    for i in range(stock_province.shape[0]):
        key = stock_province.iat[i,1]
        value = stock_province.iat[i,0]
        dict_value = stc_prvc_dict.get(key,[])
        dict_value.append(value)
        stc_prvc_dict[key] = dict_value
    return stc_prvc_dict

def get_matrix(stock_list, stock):
    '''
    Args:
        city: string 一个城市
        stocks: dataframe 所有股票对应的三个性质
    '''
    matrix = stock.loc[stock_list]
    return matrix
    
def matrix2str(matrix):
    string = '[ '
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            string += str(matrix.iat[i,j])
            string += ' , '
        string = string[:-3]
        string +=' ; '
    string = string[:-3]
#    print('for debug')
    string += ' ]'
    return string
    
def get_string_dict(stc_prvc_dict, stock):
    '''
    Args:
        stc_prvc_dict: dict 所有城市对应的股票
        stock: dataframe 所有股票对应的三个性质
    '''
    string_dict ={}
    for key, value in stc_prvc_dict.items():
        matrix = get_matrix(value, stock)
        string = matrix2str(matrix)
        dict_value = string_dict.get(key,[])
        dict_value.append(string)
        string_dict[key] = dict_value
    return string_dict

def get_stockchara(stock, stock_province, province):
    index_stockchara = list(province.iloc[:,0])
    stockchara = pd.Series([[] for i in range(province.shape[0])], index = index_stockchara)
    stc_prvc_dict = get_stc_prvc_dict(stock_province)
    string_dict = get_string_dict(stc_prvc_dict, stock)
#    for i in range(len(stockchara)):
#        stockchara.iloc[i] = string_list[i]   
    for i in range(len(stockchara)):
        stockchara.iloc[i] = string_dict[stockchara.index[i]]
        string = str(stockchara.iloc[i])[2:-2]
        stockchara.iloc[i] = string



    return stockchara
stock = stocks.loc[stock_this] # 这个也符合要求了
stock_province = pd.read_csv('./WindFunds_data/stock_province.csv',encoding='gbk')

list3= []
for i in range(stock_province.shape[0]):
    stock_code = stock_province.iloc[i,0]
    if stock_code in stock_this:
        list3.append(i)
stock_province = stock_province.iloc[list3,:]


province = pd.DataFrame(province_list_this) # 这个是符合要求的
stockchara = get_stockchara(stock, stock_province, province)
stockchara = pd.DataFrame({'province':stockchara.index, 'value':stockchara.values })
# 获得stockchara
stockchara.to_csv('./output/stockcharaRaw.csv', mode = 'w+', encoding = 'gbk')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



































