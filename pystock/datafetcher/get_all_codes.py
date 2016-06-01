#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xhb
# @Date:   2016-05-18 22:02:14
# @Last Modified by:   xhb
# @Last Modified time: 2016-05-29 17:24:23
import tushare as ts 
import os

def get_all_trading_codes():
    '''
        获取A股市场全部的交易代码和交易名称 
    '''
    all_data = ts.get_today_all()
    current_dir = os.path.dirname(__file__)
    ab_path = os.path.join( current_dir, "..\\", "..\\" )
    meta_data_path =os.path.abspath( ab_path ) + "\\meta_data\\"
    all_data[['code', 'name']].to_csv(meta_data_path+"meta_codes.csv", encoding='utf-8', index=False)

if __name__ == "__main__":
    get_all_trading_codes()
    