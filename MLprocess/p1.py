# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:21:14 2020

@author: hs101
"""
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

import numpy as np

from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import KFold
import pandas as pd

input0=pd.read_csv('./ML_output/input0.csv',encoding='gbk').set_index('index')
input1=pd.read_csv('./ML_output/input1.csv',encoding='gbk').set_index('index')

# ======================================================================== #

errdf=pd.DataFrame
# ======================================================================== #

kf = KFold(n_splits=5,shuffle=False)
for train_index, test_index in kf.split(input0):
# ======================================================================== #    
    X_train=input0.iloc[train_index,0:4]
    X_test=input0.iloc[test_index,0:4]
    y_train=input0.iloc[train_index,4]
    y_test=input0.iloc[test_index,4]

    svr = SVR(kernel='rbf',C=0.01)
    svr_y_pred = svr.fit(X_train,y_train).predict(X_test)
    y_predict = svr_y_pred
    svr_mae = mean_absolute_error(y_test,y_predict)
    svr_mse = mean_squared_error(y_test,y_predict)
    svr_rmse = np.sqrt(mean_squared_error(y_test,y_predict))

    
    rf = RandomForestRegressor()
    rf_y_pred = rf.fit(X_train, y_train).predict(X_test)
    y_predict = rf_y_pred
    rf_mae = mean_absolute_error(y_test,y_predict)
    rf_mse = mean_squared_error(y_test,y_predict)
    rf_rmse = np.sqrt(mean_squared_error(y_test,y_predict))

    
    cart = DecisionTreeRegressor()
    cart_y_pred = cart.fit(X_train, y_train).predict(X_test)
    y_predict = cart_y_pred
    cart_mae = mean_absolute_error(y_test,y_predict)
    cart_mse = mean_squared_error(y_test,y_predict)
    cart_rmse = np.sqrt(mean_squared_error(y_test,y_predict))

    
    bp = MLPRegressor()
    bp_y_pred = bp.fit(X_train, y_train).predict(X_test)
    y_predict = bp_y_pred
    bp_mae = mean_absolute_error(y_test,y_predict)
    bp_mse = mean_squared_error(y_test,y_predict)
    bp_rmse = np.sqrt(mean_squared_error(y_test,y_predict))
    err0_dict={}
    err0_dict['svr_mae']=svr_mae
    err0_dict['svr_mse']=svr_mse
    err0_dict['svr_rmse']=svr_rmse
    err0_dict['svr_mae']=svr_mae
    err0_dict['svr_mse']=svr_mse
    err0_dict['svr_rmse']=svr_rmse
    err0_dict['cart_mae']=cart_mae
    err0_dict['cart_mse']=cart_mse
    err0_dict['cart_rmse']=cart_rmse
    err0_dict['bp_mae']=bp_mae
    err0_dict['bp_mse']=bp_mse
    err0_dict['bp_rmse']=bp_rmse
    
# --------------------------------------------------------------------------- #    
    
    X_train=input1.iloc[train_index,0:5]
    X_test=input1.iloc[test_index,0:5]
    y_train=input1.iloc[train_index,5]
    y_test=input1.iloc[test_index,5]

    svr = SVR(kernel='rbf',C=0.01)
    svr_y_pred = svr.fit(X_train,y_train).predict(X_test)
    y_predict = svr_y_pred
    svr_mae = mean_absolute_error(y_test,y_predict)
    svr_mse = mean_squared_error(y_test,y_predict)
    svr_rmse = np.sqrt(mean_squared_error(y_test,y_predict))

    
    rf = RandomForestRegressor()
    rf_y_pred = rf.fit(X_train, y_train).predict(X_test)
    y_predict = rf_y_pred
    rf_mae = mean_absolute_error(y_test,y_predict)
    rf_mse = mean_squared_error(y_test,y_predict)
    rf_rmse = np.sqrt(mean_squared_error(y_test,y_predict))

    
    cart = DecisionTreeRegressor()
    cart_y_pred = cart.fit(X_train, y_train).predict(X_test)
    y_predict = cart_y_pred
    cart_mae = mean_absolute_error(y_test,y_predict)
    cart_mse = mean_squared_error(y_test,y_predict)
    cart_rmse = np.sqrt(mean_squared_error(y_test,y_predict))

    
    bp = MLPRegressor()
    bp_y_pred = bp.fit(X_train, y_train).predict(X_test)
    y_predict = bp_y_pred
    bp_mae = mean_absolute_error(y_test,y_predict)
    bp_mse = mean_squared_error(y_test,y_predict)
    bp_rmse = np.sqrt(mean_squared_error(y_test,y_predict))
    err1_dict={}
    err1_dict['svr_mae']=svr_mae
    err1_dict['svr_mse']=svr_mse
    err1_dict['svr_rmse']=svr_rmse
    err1_dict['svr_mae']=svr_mae
    err1_dict['svr_mse']=svr_mse
    err1_dict['svr_rmse']=svr_rmse
    err1_dict['cart_mae']=cart_mae
    err1_dict['cart_mse']=cart_mse
    err1_dict['cart_rmse']=cart_rmse
    err1_dict['bp_mae']=bp_mae
    err1_dict['bp_mse']=bp_mse
    err1_dict['bp_rmse']=bp_rmse
# ======================================================================== #
    print()
    




