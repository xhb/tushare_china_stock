#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xhb
# @Date:   2016-05-29 22:17:20
# @Last Modified by:   xhb
# @Last Modified time: 2016-06-01 22:23:16
import os
import pandas as pd
import datafetcher.get_all_codes
import datafetcher.get_all_daily_data
import datafetcher.get_all_intraday_data

def  update_all_daily_data():
    ''' 
           如果发现日线数据的目录里面没有对应的数据，就下载全部的历史文件。
    如果发现目录中已经存在对应的数据，那就重最新的日期更新数据。
    '''
    current_dir = os.path.dirname(__file__)
    ab_path = os.path.join( current_dir, "..\\" )
    daily_data_dir = os.path.join(ab_path, "daily_data\\")
    abs_daily_data_dir =  os.path.abspath(daily_data_dir)
    
    #获取全部codes列表
    all_code_csv = os.path.join(ab_path, "meta_data\\meta_codes.csv")
    codes_pd =  pd.read_csv(all_code_csv, dtype=str)    

    #获取已经存在的数据代码
    exists_code_list = []
    list_dirs = os.walk(abs_daily_data_dir) 
    for root, dirs, files in list_dirs:
        for csv_file in files:
            exist_file_code = csv_file.split('.')[0]
            exists_code_list.append(exist_file_code)

    #如果已经存在数据，就只做更新数据的操作，如果没有数据，就直接从开盘日下载
    pickup_code = codes_pd["code"]
    for indec, code in pickup_code.iteritems():
        if code in exists_code_list:
            datafetcher.get_all_daily_data.update_stock_data(code)
        else:
            datafetcher.get_all_daily_data.get_stock_data(code)


if __name__ == '__main__':
    update_all_daily_data()
