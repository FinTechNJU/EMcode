# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:04:28 2020

@author: hs101
"""

import pandas as pd

stock_reduce_vol_df = pd.read_csv('stock_reduce_vol_df.csv',encoding='gbk').drop(['maxReduceCode','stockPrice','maxReduceShare'],axis=1).set_index('fundCode')


fundValueRaw = pd.read_excel("基金净值.xlsx",encoding='gbk')
fundValue = pd.DataFrame()
fundValue['fundCode']=fundValueRaw['证券代码']
fundValue['fundTotalValue']=fundValueRaw.iloc[:,-1]
fundValue=fundValue.set_index('fundCode')

new = stock_reduce_vol_df.join(fundValue,how='inner')
new['percent']=abs(new.maxReduceVol/new.fundTotalValue)*100
new.to_csv('基金减持幅度.csv',encoding='gbk',mode='w+')
