# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:49:50 2020

@author: hs101
"""
import numpy as np
import pandas as pd
stock_province=pd.read_csv('./WindFunds_data/stock_province.csv',encoding='gbk')
city=pd.DataFrame()
city['index']=stock_province.iloc[:,0]
city['city']=stock_province.iloc[:,1]
city=city.set_index('index')
reduce=pd.read_csv('./基金总净值和股价减持占比_output/减持百分比.csv',encoding='gbk').set_index('fundCode')
connect=pd.read_csv('./Connections_output/new_connection.csv',encoding='gbk').set_index('manager')

def get_connectVaule_from_stock(name,stock):
    cityname= city.loc[stock]
    connectvalue=connect.loc[name,cityname]
    return connectvalue

#name='陈平'
#stock='002475.SZ'
#
#connectValue = get_connectVaule_from_stock(name,stock)    

result = reduce
result['connectValue']=[0.00 for i in range(reduce.shape[0])]

for i in range(reduce.shape[0]):
    special_case_list=[45,70]
    if i in special_case_list:
        result.iat[i,-1]= np.nan
        continue
    name=reduce.iat[i,1]
    stock=reduce.iat[i,2]
    connectValue=get_connectVaule_from_stock(name,stock)
    result.iat[i,-1]=connectValue

    

new = result.dropna(axis=0)

drop_list=[]
index_list=new.index.values.tolist()
for i in range(new.shape[0]):
    if new.iat[i,-1]==0:        
        drop_list.append(index_list[i])

new_retuslt = new.drop(drop_list,axis=0)        
new_retuslt['surePercentage']= new_retuslt.connectValue*100
new_retuslt=new_retuslt.drop(['connectValue'],axis=1)
new_retuslt['reduceIndex']=new_retuslt.surePercentage*new_retuslt.percent 
save_value=pd.DataFrame()
save_value['index']=new_retuslt.maxReduceCode
save_value['reduceIndex']=new_retuslt.reduceIndex
save_value.to_csv('./output/每股减持指标.csv',encoding='gbk',mode='w+')
