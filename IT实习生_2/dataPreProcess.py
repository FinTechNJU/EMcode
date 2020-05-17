# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import pandas as pd
dfRaw = pd.read_csv('funddata.csv',encoding = 'gbk', header = None).iloc[:,0:20]



def find(x):
    y = re.findall('\d+(?:\.\d+)?', x)[0]
#    y = round(float(y),4)
    y = float(y)
    return y
def pro(x,i):
    if(i != 3):
        return x[i]
    elif(i == 3):
        temp = x[i][2:]
        return temp
df = dfRaw

df['pro'] = df[0].apply(lambda x:x.split("\t"))
df['proo'] = df.pro.apply(lambda x : pro(x,3) )
df['coorporation'] = df.pro.apply(lambda x : pro(x,0) )
df['manager'] = df.pro.apply(lambda x : pro(x,2) )
df = df.drop('pro', axis = 1)

d = pd.DataFrame()
d["coorporation"], d["manager"] = df['coorporation'], df['manager']



str1, str2= 'code1', 'per1'
d[str1] = df.proo.apply(lambda x: x[1:])
d[str2] = df.iloc[:,1].apply(lambda x: float(x[:-1]))

for i in range(1,9):
    str1, str2 = 'code'+str(i+1), 'per'+str(i+1)
    d[str1] = df.iloc[:,2*i].apply(lambda x:x[2:])
    d[str2] = df.iloc[:,2*i+1].apply(lambda x: float(x[:-1]))

str1, str2= 'code10', 'per10'
d[str1] = df.proo.apply(lambda x: x[1:])
d[str2] = df.iloc[:,19].apply(lambda x: find(x))

funds = d
stocks = pd.read_excel("data2.xlsx")

#print(funds)
#print(stocks)

funds.to_csv("funds.csv",encoding = 'gbk',mode = 'w+')
