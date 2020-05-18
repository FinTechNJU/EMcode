# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:39:28 2020

@author: hs101
"""
'''
TODO
获得指定股票的涨跌幅，
时间界面为2019-01-02 - 2020-05-15
'''

from WindPy import w
w.start()
stock_list = 

w.wsd("600000.SH,000001.SZ,0001.HK,0020.HK", "pct_chg", "2020-01-01", "2020-05-15", "Currency=CNY")