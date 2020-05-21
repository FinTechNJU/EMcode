# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:20:45 2020

@author: hs101
"""
import pandas as pd
df1 = pd.read_csv('./Regress_output/股价控制变量.csv',encoding='gbk').set_index('index')
#df2 = pd.read_csv('./Regress_shocks/shocks.csv',encoding='gbk',header=None)
#df2.columns=['index','shocks']
#df2=df2.set_index('index')
df3 = pd.read_csv('./每个股票的减持指标_output/每股减持指标.csv',encoding='gbk').set_index('index').drop(['fundCode'],axis=1)
new=df3
#result=new.join(df1,how='inner')
#result=result.iloc
result=df3

# =========================================================== #
x1=pd.DataFrame(df1.iloc[:,0])
temp_result=result
temp_result=temp_result.join(x1,how='inner')
result['x1']=temp_result.iloc[:,-1]
# =========================================================== #


# =========================================================== #
x2=pd.DataFrame(df1.iloc[:,3])
temp_result=result
temp_result=temp_result.join(x2,how='inner')
result['x2']=temp_result.iloc[:,-1]
# =========================================================== #

# =========================================================== #
x3=pd.DataFrame(df1.iloc[:,5])
temp_result=result
temp_result=temp_result.join(x3,how='inner')
result['x3']=temp_result.iloc[:,-1]

# =========================================================== #
x4=pd.DataFrame(df1.iloc[:,6])
temp_result=result
temp_result=temp_result.join(x4,how='inner')
result['x4']=temp_result.iloc[:,-1]
# =========================================================== #

# =========================================================== #
shock=pd.DataFrame(df1.iloc[:,-1])
temp_result=result
temp_result=temp_result.join(shock,how='inner')
result['shock']=temp_result.iloc[:,-1]
# =========================================================== #





#result['shock']=result.shocks
#result=result.drop(['shocks'],axis=1)

result.to_csv('./output/input1.csv',encoding='gbk',mode='w+')

few=result.drop(['reduceIndex'],axis=1)
few.to_csv('./output/input0.csv',encoding='gbk',mode='w+')
