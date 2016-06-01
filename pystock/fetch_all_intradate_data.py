#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xhb
# @Date:   2016-06-01 22:40:07
# @Last Modified by:   xhb
# @Last Modified time: 2016-06-01 23:12:37
import os
import pandas as pd
import datafetcher.get_all_codes
import datafetcher.get_all_daily_data
import datafetcher.get_all_intraday_data

def  update_all_intradata_data():
    ''' 
           发现日线数据中没有下载完成的日内交易数据，
           下载对应日期的日内交易数据
    '''
    current_dir = os.path.dirname(__file__)
    root_path = os.path.join( current_dir, "..\\" )
    daily_data_dir = os.path.join(root_path, "daily_data\\")
    abs_daily_data_dir =  os.path.abspath(daily_data_dir)
    
    intra_data_dir =  os.path.join(root_path, "intradate_data\\")
    abs_intra_data_dir =  os.path.abspath(intra_data_dir)

    #获取已经存在的日线数据代码
    list_dirs = os.walk(abs_daily_data_dir) 
    for root, dirs, files in list_dirs:
        for csv_file in files:
            exist_code = csv_file.split('.')[0]
            #读取已经下载完成的日线数据的csv文件，获取index
            exist_daily_csv_file = abs_daily_data_dir + "\\" + csv_file 
            exist_data = pd.read_csv(exist_daily_csv_file,  index_col=0) 

            #根据index的日期组成绝对路径，查看对应日内数据的数据是否存在，不存在就下载
            for day in exist_data.index:
                intradate_csv_file = abs_intra_data_dir + "\\" + exist_code + "\\" + day + ".csv"
                if not os.path.exists(intradate_csv_file ):
                    datafetcher.get_all_intraday_data.get_stock_intraday_data( exist_code, day )


if __name__ == '__main__':
    update_all_intradata_data()
