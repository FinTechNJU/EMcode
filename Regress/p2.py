# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:51:29 2020

@author: hs101
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:01:47 2020

@author: hs101
"""
'''
寻找相关变量
'''

import pandas as pd

duRaw = pd.read_csv('./shocks/shocks.csv', encoding = 'gbk',header = None)
agRaw = pd.read_excel('A股属性.xlsx',encoding = 'gbk')
hgRaw = pd.read_excel('H股属性.xlsx',encoding = 'gbk')


du = duRaw
ag = agRaw
hg = hgRaw
stock_list = list(du.iloc[:,0])

def which_side(stock):
    exchange = stock[-2:]
    if exchange == "SZ":
        side = 0
    elif exchange == "SH":
        side = 0
    elif exchange == "HK":
        side = 1
    return side

attribute_length = ag.shape[1] - 2

attribute_name = list(ag.columns[2:])
stock_attribute_df = pd.DataFrame()
for i in range(attribute_length):
    stock_attribute_df[attribute_name[i][:3]] = [0.00 for i in range(du.shape[0])]
stock_attribute_df["duvol"] = du.iloc[:,1]
stock_attribute_df['index'] = du.iloc[:,0]
stock_attribute_df=stock_attribute_df.set_index('index')

# ============================================================================== #
for i in range(du.shape[0]):
#    print(i)
    code = du.iloc[i,0]  
    side = which_side(code)
    if side == 0:
        exchg = ag
    elif side == 1:
        exchg = hg
    for j in range(exchg.shape[0]):
        if exchg.iloc[j,0] == code:
            for k in range(attribute_length):
                stock_attribute_df.iat[i,k] = exchg.iat[j,k+2]

stock_attribute_df = stock_attribute_df.fillna(0)
stock_attribute_df.to_csv('./output/股价控制变量.csv',encoding='gbk',mode='w+')
# ============================================================================== #




































# ============================================================================== #

















