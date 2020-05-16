# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:35:48 2020

@author: hs101
"""
'''
展示指数的数据
'''

import pandas as pd
index = pd.read_excel("indexGet.xlsx", encoding = 'gbk')

def show(df):
    def draw(dataframe): 
        return True
    def get_min(df):
        show_dict = {}
        for i in range(1,df.shape[1]):
            show_dict[df.columns[i]] = df.iloc[:,i].min()
        return show_dict
    def get_max(df):
        show_dict = {}
        for i in range(1,df.shape[1]):
            show_dict[df.columns[i]] = df.iloc[:,i].max()
        return show_dict
    def get_std(df):
        show_dict = {}
        for i in range(1,df.shape[1]):
            show_dict[df.columns[i]] = df.iloc[:,i].std()
        return show_dict
    def get_count(df):
        show_dict = {}
        for i in range(1,df.shape[1]):
            show_dict[df.columns[i]] = df.iloc[:,i].count()
        return show_dict
    dict_all = {}
    dict_all['max'] = get_max(df)
    dict_all['count'] = get_count(df)
    dict_all['std'] = get_std(df)
    dict_all['min'] = get_min(df)
    return dict_all
if __name__ == "__main__":
    dict_index = show(index)