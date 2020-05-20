# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:42:09 2020

@author: hs101
"""

import pandas as pd
connection = pd.read_csv('./output/connection.csv', encoding='gbk').set_index('manager')

# ============================================================================ #
'''归一化处理
'''        


def guiyi(connection):
    new_connection = connection
    for i in range(connection.shape[1]):
        maxValue = connection.iloc[:,i].max()
        for j in range(connection.shape[0]):
            new_connection.iat[j,i] = new_connection.iat[j,i]/maxValue
    return new_connection
new_connection = guiyi(connection)
#new_connection= new_connection.dropna(axis=1)

# ============================================================================ #

new_connection.to_csv('./output/new_connection.csv', encoding='gbk',mode='w+')
