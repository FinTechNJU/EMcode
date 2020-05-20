# -*- coding: utf-8 -*-
"""
Created on Thu May 21 01:42:47 2020

@author: hs101
"""
import statsmodels.formula.api as sm
import pandas as pd


input1=pd.read_csv('./ML_output/input1.csv',encoding='gbk').set_index('index')


forcast=input1
simple = sm.ols(formula = 'shock ~ x1 ', data = forcast).fit()
print(simple.summary())
