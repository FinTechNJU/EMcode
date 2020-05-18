# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:04:17 2020

@author: hs101
"""


import pandas as pd
dataRaw1 = pd.read_csv("stocks.csv",encoding = 'gbk',index_col=0)
dataRaw3 = pd.read_csv('cities.csv',encoding = 'gbk').drop(["Unnamed: 0"],axis =1)
dataRaw5 = pd.read_csv('stock_province.csv', encoding = 'gbk').drop(['EV3', 'PB_LYR', 'EPS_TTM'], axis =1)


def get_stc_prvc_dict(stock_province):
    stc_prvc_dict = {}
    for i in range(stock_province.shape[0]):
        key = stock_province.iat[i,1]
        value = stock_province.iat[i,0]
        dict_value = stc_prvc_dict.get(key,[])
        dict_value.append(value)
        stc_prvc_dict[key] = dict_value
    return stc_prvc_dict


def for_testing():
    
    print('for debug')
    
    
    
    
    
    pass



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
    
def get_string_list(stc_prvc_dict, stock):
    '''
    Args:
        stc_prvc_dict: dict 所有城市对应的股票
        stock: dataframe 所有股票对应的三个性质
    '''
    string_list = []
    for key, value in stc_prvc_dict.items():
        matrix = get_matrix(value, stock)
        string = matrix2str(matrix)
        string_list.append(string)
    return string_list

def get_stockchara(stock, stock_province, province):
    stockchara = pd.Series([[] for i in range(province.shape[0])])
    stc_prvc_dict = get_stc_prvc_dict(stock_province)
    assert len(stc_prvc_dict) == 31 
    # 有31个省份
    string_list = get_string_list(stc_prvc_dict, stock)
    for i in range(len(stockchara)):
        stockchara.iloc[i] = string_list[i]    
    return stockchara
    

if __name__ == "__main__":
    stock = dataRaw1
    province = dataRaw3
    stock_province = dataRaw5
    stockchara = get_stockchara(stock, stock_province, province)
    stockchara.to_csv('stockchara.csv', mode = 'w+', encoding = 'gbk')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    