# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class stock_history_data(object):

    """
    每只股票针对时间的其他维度的折线图
    返回list类型各个维度的值
    """

    def stock_data(self, file_name):
        # 读取csv文件并转换成utf-8编码
        df_1 = pd.read_csv('gupiao/data/data_complete/' + file_name, encoding='utf-8')
        # 获取列表字段 开盘价(元),收盘价(元),最低价(元),最高价(元),涨跌幅(%
        col_1 = ['日期', '开盘价(元)', '收盘价(元)', '最低价(元)', '最高价(元)', '涨跌幅(%)']
        # 生成新dataframe
        df_1 = df_1[col_1]

        # 日期（datetime类型）
        x_date = pd.to_datetime(df_1['日期'])
        # 日期立标
        # 开盘价列表
        y_open = list(df_1['开盘价(元)'])
        # 收盘价列表
        y_close = list(df_1['收盘价(元)'])
        # 最低价列表
        y_low = list(df_1['最低价(元)'])
        # 最高价列表
        y_high = list(df_1['最高价(元)'])

        # ub_axix = filter(lambda x: x % 200 == 0, x_date)
        plt.figure()
        plt.title('Stock Data')
        plt.plot(x_date, y_open, color='blue', label='open')
        # plt.plot(x_date, y_close, color='red', label='close')
        plt.plot(x_date, y_high, color='green', label='high')
        # plt.plot(x_date, y_low, color='blue', label='low')
        plt.legend()  # 显示图例
        plt.xlabel('date')
        plt.ylabel('price')

        plt.savefig('static/img/history/'+"history_"+file_name+'.png')
        #plt.show()

        return list(x_date), y_open, y_low, y_high, y_close
#
# if __name__ == '__main__':
#     ra = stock_history_data()
#     ra.stock_data('000010.SZ.CSV')