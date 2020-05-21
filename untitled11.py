# -*- coding: utf-8 -*-
"""
Created on Thu May 21 01:28:28 2020

@author: hs101
"""
def score(b,a,dimension):       
# a is predict, b is actual. dimension is len(train[0]).
    aa=a.copy(); bb=b.copy()
    if len(aa)!=len(bb):
        print('not same length')
        return np.nan

    # RR means R_Square
    RR=1-sum((bb-aa)**2)/sum((bb-np.mean(bb))**2)

    n=len(aa); p=dimension
    Adjust_RR=1-(1-RR)*(n-1)/(n-p-1)
    # Adjust_RR means Adjust_R_Square

    return Adjust_RR

#

    bp_r2 = sklearn.metrics.r2_score(y_true, y_pred)
    num_chara = input0.shape[1] -1
    bp_adjr2 = score(y_true, y_pred,num_chara)
    
        cart_r2 = sklearn.metrics.r2_score(y_true, y_pred)
    num_chara = input0.shape[1] -1
    cart_adjr2 = score(y_true, y_pred,num_chara)
    
        rf_r2 = sklearn.metrics.r2_score(y_true, y_pred)
    num_chara = input0.shape[1] -1
    rf_adjr2 = score(y_true, y_pred,num_chara)
    
        svr_r2 = sklearn.metrics.r2_score(y_true, y_pred)
    num_chara = input0.shape[1] -1
    svr_adjr2 = score(y_true, y_pred,num_chara)