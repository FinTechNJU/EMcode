# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:47:42 2020

@author: hs101
"""
'''
Purpose:
    获得portweight.csv
Dependency:
    None
'''


import pandas as pd
def get_dataRaw_list():
#    dataRaw_list = [pd.DataFrame]
#    names = locals()
    dataRaw1 = pd.read_csv("stocks.csv",encoding = 'gbk')
    dataRaw2 = pd.read_csv("funds.csv",encoding = 'gbk').drop(["Unnamed: 0"],axis =1)
    dataRaw3 = pd.read_csv('cities.csv',encoding = 'gbk').drop(["Unnamed: 0"],axis =1)
    dataRaw4 = pd.read_csv("managers.csv", encoding = 'gbk').drop(['Unnamed: 0'],axis =1)
    dataRaw5 = pd.read_csv('stock_province.csv', encoding = 'gbk').drop(['EV3', 'PB_LYR', 'EPS_TTM'], axis =1)
    dataRaw6 = pd.read_csv("fundCity.csv",encoding = 'gbk').drop(["Unnamed: 0"],axis =1)
#    for i in range(1,len(names)-1):
#        '''减去三是因为有三个变量 names dataRawList
#        加一是因为range右边是开的
#        这里len(names) -1 = 7
#        '''
#        dataRaw_list.append(names['dataRaw%s'%(i)])
    dataRaw_list = [pd.DataFrame(), dataRaw1, dataRaw2, dataRaw3, dataRaw4, dataRaw5, dataRaw6]
    return dataRaw_list

def check_1(province_stockList_dict):
    '''查看province_stockList_dict是否返回正确
    '''
    length = 0
    for value in province_stockList_dict.values():
        length += len(value)
    assert length == 668
def check_2(pw, province_stockList_dict):
    '''查看pw是否返回正确
    '''
    i =1 # 用于记录循环的次数,pw第一位是基金经理的名字
    for key, value in province_stockList_dict.items():
        test_cell = pw.iloc[0,i]
        assert len(value) == len(test_cell)
        i +=1 # 用于记录循环的次数 
     
def delete_few_province(pw):
    delete_list = [1, 8, 11, 12, 14, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31]
    drop_name_list = []
    for i in range(len(delete_list)):
        item = pw.columns[delete_list[i]]
        drop_name_list.append(item)
    result = pw.drop(drop_name_list, axis =1)
    print("test")
    return result
    
    
def get_province_stockList_dict(stock_province):
    '''获得{城市：[股票]}
    Args:
        stock_province: dataframe stock-province
    returns:
        {province: [stock1,stock2, ... ]
    '''
    province_stockList_dict = {}
    for i in range(stock_province.shape[0]):
        line = stock_province.iloc[i,:]
        for j in range(1):
            key = line[j+1]
            value = line[j]
            dict_value = province_stockList_dict.get(key,[])
            dict_value.append(value)
            province_stockList_dict[key] = dict_value
            
    return province_stockList_dict

def set_portweight(null_pw, fund, fundCity, province_stockList_dict):
    '''由空dataframe 得到满足条件的dataframe
    Returns:
        dataframe
            row: N个经理
            column: K个城市
            content: 一个list
                经理N在K城市所有股票的权重，没有的股票设置为0
                
    '''
    def get_wgt_dict(line):
        wgt_dict = {}
        for j in range(10):
            '''生成对应字典
            '''
            key = line[2*j+3] # 找到省份
            value = line[2*j+4] # 找到省份对应的权重
            dict_value = wgt_dict.get(key, [])
            dict_value.append(value)
            wgt_dict[key] = dict_value
        return wgt_dict
            
    pw = null_pw
    for i in range(fund.shape[0]):
        line1 = fund.iloc[i,:]
        line2 = fundCity.iloc[i,:]
        wgt_dict1 = get_wgt_dict(line1 )
        wgt_dict2 = get_wgt_dict(line2 )
        
        count = 0 # 用于记录循环的次数
        for key, value in province_stockList_dict.items():
            my_value2 = wgt_dict2.get(key, []) # 得到该经理再该城市的股票权重
            if  len(my_value2) ==0:
                '''如果该基金经理没有持有该城市的股票，那么该向量全设为零
                '''
                pw.iat[i,count+1] = [ 0.00 for i in range(len(value))]
             
            # 如果有该城市的股票，计算权重
            weight_list = [0.00 for i in range(len(value))]
            for j in range(len(value)):
                for tmp_key, tmp_value in wgt_dict1.items():
                    if tmp_key == value[j]:
                        weight_list[j] = tmp_value[0]
            pw.iat[i,count+1] = weight_list
            count +=1 # 用于记录循环的次数        
    return pw



def get_null_portweight(fundCity, city):
    pw = pd.DataFrame()
    pw['manager'] = fundCity.iloc[:,2]
    for i in range(city.shape[0]):
        province = city.iloc[i,0]
        pw[province] = pd.Series(pd.Series([[] for i in range(fundCity.shape[0])]))
    assert pw.shape == (259, 32)
    # 检查空dataframe是否生成正确
    return pw



if __name__ == "__main__":
    dataRaw_list = get_dataRaw_list()
    
    fund = dataRaw_list[2]
    stock = dataRaw_list[1]
    city = dataRaw_list[3]
    manager = dataRaw_list[4]
    stock_province = dataRaw_list[5]
    fundCity = dataRaw_list[6]
    
    
    province_stockList_dict = get_province_stockList_dict(stock_province)
    check_1(province_stockList_dict)
    
    
    null_pw = get_null_portweight(fundCity, city)
    pw = set_portweight(null_pw,fund, fundCity, province_stockList_dict)
    check_2(pw, province_stockList_dict)
    
    pw = pw.applymap(str)
    
    pw_few = delete_few_province(pw)
    pw.to_csv('portweight.csv',mode = 'w+', encoding = 'gbk')
    pw_few.to_csv('portweight_few.csv',mode = 'w+', encoding = 'gbk')










































