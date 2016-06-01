#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xhb
# @Date:   2016-05-18 23:02:26
# @Last Modified by:   xhb
# @Last Modified time: 2016-06-01 22:10:23
import tushare as ts 
import os
import time
import pandas as pd
import datetime

def get_stock_data(code):
    """
         获取一只股票的全部历史数据，让后保存到csv文件中
    """
    df = ts.get_stock_basics()
    str_date_to_market =  str(df.ix[code]['timeToMarket'])
    time_date_to_market = time.strptime(str_date_to_market, "%Y%m%d")
    date_to_market = time.strftime("%Y-%m-%d", time_date_to_market) 
    today = time.strftime("%Y-%m-%d", time.localtime()) 
    data_frame = ts.get_h_data(code, start=date_to_market, end=today)
    current_dir = os.path.dirname(__file__)
    ab_path = os.path.join( current_dir, "..\\", "..\\" )
    save_path = os.path.abspath(ab_path) + "\\daily_data\\" +  code + ".csv"
    data_frame.to_csv(save_path, encoding='utf-8')

def update_stock_data(code):
    """
         获取一只股票的全部历史数据，让后保存到csv文件中
    """
    current_dir = os.path.dirname(__file__)
    ab_path = os.path.join( current_dir, "..\\", "..\\" )
    save_path = os.path.abspath(ab_path) + "\\daily_data\\" +  code + ".csv"
    save_data = pd.read_csv(save_path,  index_col=0,  parse_dates=True)

    last_update_date_time = save_data.head(1).index[0]
    last_update_date_p1_time = last_update_date_time + datetime.timedelta(days=1)

    last_update_date_p1 = time.strftime("%Y-%m-%d", last_update_date_p1_time.timetuple()) 
    today = time.strftime("%Y-%m-%d", time.localtime()) 
    data_frame = ts.get_h_data(code, start=last_update_date_p1, end=today)
    
    if data_frame is None:
        print "{0} don't need to update".format(code)
    else:    
        all_data_frame = data_frame.append( save_data )
        all_data_frame.to_csv(save_path, encoding='utf-8')

if  __name__ == '__main__':
    update_stock_data("000001")

