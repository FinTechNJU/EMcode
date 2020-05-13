# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:34:46 2020

@author: hs101
"""

'''
Purpose:
    处理wind下载下来的数据，得到基金的csv
    看看有多少个不同的基金经理
'''

import pandas as pd
dataRaw = pd.read_excel('WindFunds.xlsx')



class Count:
    name_dict = {}
    
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.line = []
    
    def __str__(self):
        lines = ''
        for item in self.line:
            lines += ' _' + str(item) + '_ '
        return ">>> name: %s ... count: %d ... line: %s"%(self.name, self.count, lines)
#        return ">>> name: %s ... count: %d "%(self.name, self.count)
        
    def add(self, num):
        self.count += 1
        self.line.append(num)


        
def main():        
    fund = dataRaw
    name = fund.iloc[:,2]
    name_list = []
    for item in name:
        if(item not in name_list):
            name_list.append(item)
    #    print(type(item))
    #print(len(name_list))
    
    length = fund.shape[0]
    for i in range(length):
        name = fund.iloc[i,2]
        if name in Count.name_dict.keys():
            value = Count.name_dict[name]
            value.add(i)
        if name not in Count.name_dict.keys():
            count = Count(name)
            count.add(i)
            Count.name_dict[name] = count
    name_df = pd.DataFrame(name_list)
    name_df.to_csv("managers.csv", mode = 'w+',encoding = 'gbk')
            
    drop_list = []
    for item in Count.name_dict.values():
        if len(item.line) >= 2:
            drop_list.extend(item.line[1:])
            # 出现重复的基金经理，保留第一个，其余的省略
    assert len(drop_list) + len(name_list) == fund.shape[0]
    funds = fund.drop(drop_list)    
    funds.to_csv("funds.csv", mode = 'w+',encoding = 'gbk')
    funds.to_csv("funds_matlab.csv", mode = 'w+',encoding = 'gbk', header= None)

if __name__ == "__main__":
    main()



