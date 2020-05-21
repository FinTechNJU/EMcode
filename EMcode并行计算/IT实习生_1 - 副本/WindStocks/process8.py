# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:08:38 2020

@author: hs101
"""

'''
获得股票收益率低于、高于市场的天数
'''
import pandas as pd
#import numpy as np
residualRaw = pd.read_csv('./shocks/stock_residual.csv',encoding='gbk', index_col = 0, header = 0)
res_shockRaw = pd.read_csv('./shocks/res_shock.csv',encoding='gbk', index_col = 0, header = 0)

index_getRaw = pd.read_excel("indexGet.xlsx", encoding = 'gbk', index_col = 0)

# ================================================================================================= #

res = residualRaw
res_shock = res_shockRaw
index_get = index_getRaw

def which_side(stock):
    key = pd.DataFrame(stock).columns.values.tolist()[0]
    side = key[-2:]
    if side == 'SH':
        which_side = 0
    elif side == 'SZ':
        which_side = 0
    elif side == 'HK':
        which_side = 1
    return which_side


result = pd.DataFrame()
result['stock_code'] = ["" for i in range(res.shape[1])] # 对于121个股票
result['plus_euqal'] = [[] for i in range(res.shape[1])] # 对于121个股票
result['minus'] = [[] for i in range(res.shape[1])] # 对于121个股票

for i in range(res.shape[1]):
    # 对于121个股票
    
    def find_index(sr):
        index_list = []
        for i in range(len(sr)):
            if sr.iloc[i] == True:
                index_list.append(i)
        return index_list   
    stock = res.iloc[:,i]
    name = pd.DataFrame(stock).columns.values.tolist()[0]
    side = which_side(stock)
    index_ = index_get.iloc[:,side]
    
    plus_df = stock >= index_
    plus_df_sum = plus_df.astype(int).sum()
    plus_index_list = find_index(plus_df)
    
    minus_df = stock < index_
    minus_df_sum = minus_df.astype(int).sum()
    minus_index_list = find_index(minus_df)
        
    assert plus_df_sum + minus_df_sum == index_.shape[0]
    assert len(minus_index_list) == minus_df_sum
    assert len(plus_index_list) == plus_df_sum
    
    result.iloc[i,0] = name
    result.iloc[i,1] = plus_index_list
    result.iloc[i,2] = minus_index_list
    
    
    
result.set_index(["stock_code"],inplace = True)
result.to_csv("./shocks/stocks_days.csv", encoding = 'gbk')



