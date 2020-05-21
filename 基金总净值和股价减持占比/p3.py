# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:23:38 2020

@author: hs101
"""

import pandas as pd

path = 'Full_data_WindStocks_data_matlab_set_up'
maxReduce = pd.read_csv('./'+path+'/newMaxReduce.csv',encoding='gbk').drop(['Unnamed: 0'],axis = 1).set_index('fundCode')
old=pd.read_csv('基金减持幅度.csv',encoding='gbk').set_index('fundCode')
new1 = maxReduce.join(old,how='inner')
#new12 = maxReduce.join(old,how='outer')
new1.to_csv('./output/减持百分比.csv',encoding='gbk',mode='w+')
