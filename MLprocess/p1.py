# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:21:14 2020

@author: hs101
"""




import pandas as pd
input0=pd.read_csv('./ML_output/input0.csv',encoding='gbk').set_index('index')
input1=pd.read_csv('./ML_output/input1.csv',encoding='gbk').set_index('index')

from sklearn.svm import SVR
svr=SVR(kernel='rbf',C=1)
svr_y_pred=svr_rbf.fit(X_train,y_train).predict(X_test)