# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:31:40 2020

@author: hs101
"""

'''
获得股票duvol
'''
import re
import pandas as pd
import numpy as np
res_shockRaw = pd.read_csv('./shocks/res_shock.csv',encoding='gbk', index_col = 0, header = 0)
res_dayRaw = pd.read_csv('./shocks/stocks_days.csv',encoding='gbk', index_col = 0, header = 0)


# ================================================================================================= #

res_shock = res_shockRaw
res_day = res_dayRaw
duvol_dict = {}
for i in range(res_shock.shape[1]):
    # 对于所有股票
    def get_sum(stock, line_list):
        def string2list(line_list):
            line_list = [int(s) for s in re.findall(r'\d+',line_list)]
            return line_list
        line_list = string2list(line_list)
        result = stock.iloc[line_list]
        result = np.square(result) 
        result = result.sum()
        return result
    stock = res_shock.iloc[:,i]
    line = res_day.iloc[i,:]
    
    sum0 = get_sum(stock, line[0]) # Up
    sum1 = get_sum(stock, line[1]) # Down

    duvol_inside_left = (len(line[0]) -1 ) * sum1
    duvol_inside_right = (len(line[1]) -1 ) *sum0
    duvol = np.log( duvol_inside_left / duvol_inside_right )
    name = pd.DataFrame(stock).columns.values.tolist()[0]
    duvol_dict[name] = duvol *100 # 放大指标， 方便观察
    

duvol_sr = pd.Series(duvol_dict)
duvol_sr.to_csv('./shocks/shocks.csv', encoding = 'gbk')    

