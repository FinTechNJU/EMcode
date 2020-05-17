# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:40:51 2020

@author: hs101
"""
'''
获得 [基金，基金经理，减持最大票，减持份额]
'''
import pandas as pd
def get_result_from_reduce():
    reduce = pd.read_excel("reduceShare.xlsx", encoding = 'w+')
    
    result = pd.DataFrame()
    
    key_list_all = []
    value_list_all = []
    for i in range(reduce.shape[0]):
        key_list = []
        value_list = []
        line = reduce.iloc[i,:]
        for j in range(10):
            key_list.append(line[2*j+3])
            value_list.append(line[2*j+4])
        print(" ")
        index = value_list.index(min(value_list))
        key = key_list[index]
        value = value_list[index]
        key_list_all.append(key)
        value_list_all.append(value)
        
    key = pd.Series(key_list_all)
    value = pd.Series(value_list_all)
    
    result['fundCode'] = reduce.iloc[:,0]
     
    result['fundName'] = reduce.iloc[:,1]
    
    result['manager'] = reduce.iloc[:,2]   
    
    result['maxReduceCode'] = key
    
    result['maxReduceShare'] = value
    return result 
if __name__== "__main__":
    result = get_result_from_reduce()
    cleaned = result.dropna()
    cleaned.to_csv("maxReduce.csv", mode = 'w+', encoding = 'gbk')