# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:34:46 2020

@author: hs101
"""
from WindPy import w
import pandas as pd
w.start()
path = 'Full_data_WindStocks_data_matlab_set_up'
maxReduce = pd.read_csv('./'+path+'/newMaxReduce.csv',encoding='gbk').drop(['Unnamed: 0'],axis = 1).set_index('fundCode')

def get_stock_reduce_vol_df(stock_code_sr, maxReduceShare):
    '''
    Args:
        stock_code_sr, series
        maxReduceShare, series
    '''
    def special(df):
        df.loc['019611.SH']=100.013
        df.loc['018007.SH']=100.700
        return df
    assert len(set(stock_code_sr)) == len(stock_code_sr)
    stock_code_list = list(stock_code_sr)
    stock_price_df = w.wss(stock_code_list, "vwap","tradeDate=20200519;cycle=Y;priceAdj=U",usedf=True)[1]
    stock_price_df=special(stock_price_df)
    fund_df = pd.DataFrame(stock_code_sr)
    fund_df['stockPrice']= stock_price_df.VWAP.values.tolist()
    fund_df['maxReduceShare']= maxReduceShare.values.tolist()
    fund_df['maxReduceVol']= fund_df.stockPrice * fund_df.maxReduceShare
    return fund_df
    

stock_code_sr = maxReduce.maxReduceCode
maxReduceShare = maxReduce.maxReduceShare

stock_reduce_vol_df = get_stock_reduce_vol_df(stock_code_sr, maxReduceShare) 
stock_reduce_vol_df.to_csv('stock_reduce_vol_df.csv',encoding='gbk',mode='w+')
