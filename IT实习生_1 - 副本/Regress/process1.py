# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:01:47 2020

@author: hs101
"""
'''
寻找相关变量
'''
import pandas as pd
from WindPy import w
w.start()
duRaw = pd.read_csv('./shocks/shocks.csv', encoding = 'gbk',header = None)


du= duRaw
stock_list = list(du.iloc[:,0])
