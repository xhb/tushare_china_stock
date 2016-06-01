#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xhb
# @Date:   2016-05-26 23:43:22
# @Last Modified by:   xhb
# @Last Modified time: 2016-05-29 17:30:37
import tushare as ts 
import os
import time
import sys

def get_stock_intraday_data(code, date):
    """
         获取一只股票的历史某天的日内交易数据，让后保存到csv文件中
    """
    data_frame = ts.get_tick_data(code, date=date)
    current_dir = os.path.dirname(__file__)
    ab_path = os.path.join( current_dir, "..\\", "..\\" )
    data_root_path = os.path.abspath( ab_path ) + "\\intradate_data\\"
    code_path = data_root_path + code
    if not os.path.exists(code_path): 
        os.makedirs(code_path)
    save_path = code_path + "\\" + date + ".csv"
    data_frame.to_csv(save_path, encoding='utf-8', index=False)

if  __name__ == '__main__':
    get_stock_intraday_data("000001", "2016-05-18")

