# -*- coding: utf-8 -*-
"""
Created on Thu May 21 01:42:47 2020

@author: hs101
"""
import statsmodels.formula.api as sm
import pandas as pd


input1=pd.read_csv('./ML_output/input1.csv',encoding='gbk').set_index('index')

#forcast=pd.DataFrame()
#forcast['x1']=input1.iloc[:,1]
#forcast['shock']=input1.iloc[:,-1]
forcast=input1
simple = sm.ols(formula = 'shock ~ reduceIndex', data = forcast.iloc[:9]).fit()
print(simple.summary())
