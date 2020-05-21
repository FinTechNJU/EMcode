# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:00:41 2020

@author: hs101
"""
'''
从wind获得股票一年内的收益率
从文件中读入整个市场的平均收益率，用指数来代替
利用回归获得每支股票每天的特定的收益
利用股票的特定收益率，得到股票的崩盘指标
Attention：
    因为要涉及到回归，每次结果不同，不要轻易运行
'''

import numpy as np
from WindPy import w
import pandas as pd
import statsmodels.formula.api as sm

w.start()

newStockRaw = pd.read_csv("./matlab_set_up/newStock.csv", encoding = 'gbk').iloc[:,2]
stock_listRaw = list(newStockRaw)
stock_dfRaw = w.wsd(stock_listRaw, "pct_chg", "2019-01-01", "2020-05-15", "Currency=CNY",usedf= True)[1]
index_getRaw = pd.read_excel("indexGet.xlsx", encoding = 'gbk')


class Residual:
    def __init__(self,stock, index_):
        self.index_ = index_
        self.stock = stock
        self.residual = None
        self.get_residual()
        
    def get_residual(self):
        '''
        Args:
            stock
            index_
        '''
        df = pd.DataFrame
        df_left = self.stock
        df_right = self.index_
        df = pd.concat([df_left, df_right],axis =1, ignore_index = True)
        df.columns =['stock_return', 'index_return']
        
        simple = sm.ols(formula = 'stock_return ~ index_return',data = df).fit()
        # 回归的时候 左边是因变量，右边是自变量
        self.residual = simple.resid
        # 获得残差
    
class All_Residual:
    '''
    Depends:
        Residual, class
    '''
    def __init__(self, stock_df, index_get):
        self.stock_df = stock_df
        self.index_get = index_get
        self.residual_df = None
        self.get_residual_dict()

        
    def get_residual_dict(self):  
        '''
        Args:
            stock_df, dataframe
            index_get, dataframe
        '''
        res_dict ={}
        for i in range(self.stock_df.shape[1]):
            print(">>> In Process: NO ... %d"%i)
            # TODO debug
#            stock.df
            
            # TODO debug
            stock = self.stock_df.iloc[:,i].reset_index(drop=True)
            key = pd.DataFrame(stock).columns.values.tolist()[0]
            side = key[-2:]
            if side == 'SH':
                which_side = 1
            elif side == 'SZ':
                which_side = 1
            elif side == 'HK':
                which_side = 2
            index_ = self.index_get.iloc[:,which_side] # which_side = 1 大陆， which_side = 2 港股
            res = Residual(stock,index_)
            value = res.residual
            res_dict[key] = value 
        print("Done")
        self.residual_df = pd.DataFrame(res_dict)
        
def to_fillna(stock_df):
    '''
    每一列股票的缺失值，用股票在一年内的均值代替
    '''
    stock_df = stock_df.apply(lambda x:x.fillna(x.mean()) ,axis=0)
    return stock_df


if __name__=="__main__":
    newStock = newStockRaw
    stock_list = stock_listRaw
    stock_df = stock_dfRaw
    index_get = index_getRaw
    
    stock_df = to_fillna(stock_df) # 每一列股票的缺失值，用股票在一年内的均值代替

    all_residual = All_Residual(stock_df, index_get)
    all_res_df = all_residual.residual_df
    all_res_df.index = stock_df.index    
    all_res_df.to_csv("./shocks/stock_residual.csv", mode='w+',encoding = 'gbk')
    
    res_shock = all_res_df.apply(lambda x:np.log(x/100 + 1) )
    res_shock.to_csv("./shocks/res_shock.csv", mode='w+',encoding = 'gbk')

    



















    