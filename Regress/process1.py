# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:01:47 2020

@author: hs101
"""
'''
寻找相关变量
'''

import statsmodels.formula.api as sm
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

# ============================================================================== #


result_dict = {}
def show(i):
    forcast = pd.DataFrame()
    forcast['x'] = stock_attribute_df.iloc[:,i]
    forcast['duvol'] = stock_attribute_df.iloc[:,-1]
    simple = sm.ols(formula = 'duvol ~ x', data = forcast).fit()
    print(simple.summary())
# ============================================================================== #
i = 0
show(i)
# ============================================================================== #









# ============================================================================== #
number_list= [0.024, 0.554, 0.096, 0.022, 0.149, 0.005,0.002,0.492,0.836]
result_dict[i] = number_list[-1]
result = pd.Series(index = list(ag.columns[2:]), data = number_list )
result = pd.DataFrame(result)
result.columns = ['P>|t|']
result.to_csv('P_value_of_attributes.csv', encoding = 'gbk', mode = 'w+')










































