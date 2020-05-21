# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:12:26 2020

@author: hs101
"""
import re
import pandas as pd

'''
(1)计算一个人在一个城市与另一个特定的人的关系数
(2)计算一个人在某个城市的所有人的关系数字 
(3)然后对所有城市循环 j
(4)然后对所有人循环 i
(5)最后得到一个[不同人 x 不同城市]的矩阵
'''

#connectionCopy = pd.read_csv('./output/connection.csv',encoding='gbk')

pw = pd.read_csv('./Full_Data_output/portweightRaw.csv',encoding='gbk')
pw=pw.set_index('manager')



connection = pd.DataFrame()
for i in range(pw.shape[1]):
    name  = pw.columns.values.tolist()[i]
    connection[name] = [0.00 for i in range(pw.shape[0])]
connection.index = pw.index

def demand_1(other, main):
    '''(1)计算一个人在一个城市与另一个特定的人的关系数
    Args:
        other
        main
    '''
    assert len(main) == len(other)
    length = len(main)
    result = []
    for l in range(length):
        if other[l]>0 and main[l]>0:
            temp = min(other[l] , main[l])
            result.append(temp)
    result_sum = sum(result)
    result_return = result_sum/length 
    return result_return

def str2float_list(other):
    '''一个string 转成一个list
    '''
    result = []
    temp = re.findall(r'\d+.\d+',other)
    for item in temp:
        result.append(float(item))
    return result

for i in range(pw.shape[0]):
    '''i是基金经理'''
    for j in range(pw.shape[1]):
        '''j是省份'''
        print("(%d, %d)"%(i,j))
        if i==0 and j ==1:
            print()
        column = pw.iloc[:,j]
        main = column.iloc[i]
        manager_index_list=set([i for i in range(pw.shape[0])])
        manager_index_list=list(manager_index_list.difference(set([i])))        
        others = column.iloc[manager_index_list]
        main = str2float_list(main)
        #k = 0
        demand_2 = 0
        #(2)计算一个人在某个城市的所有人的关系数字
        for k in range(len(others)):
            other = others.iloc[k]
            other = str2float_list(other)
#            demand_1
            demand_1_num = demand_1(other, main)
            demand_2 += demand_1_num
        #(2)计算一个人在某个城市的所有人的关系数字
        connection.iat[i,j] = demand_2



connection.to_csv('./output/connection.csv',mode='w+',encoding='gbk')

















