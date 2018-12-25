# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class radar_pic(object):

    def get_stock_dic(self, csv_name):
        # 读取csv文件并转换成utf-8编码
        df_1 = pd.read_csv('gupiao/data/data_complete/'+csv_name, encoding='utf-8')
        # 获取列表字段 开盘价(元),收盘价(元),最低价(元),最高价(元),涨跌幅(%
        col_1 = ['开盘价(元)', '收盘价(元)', '最低价(元)', '最高价(元)', '涨跌幅(%)']
        # 生成新dataframe
        df_1 = df_1[col_1]
        # 取最新100条数据求各列平均值并封装成字典
        df_lastest_100 = df_1[-100:]
        df_mean = df_lastest_100.mean(axis=0)
        np_mean = np.array(df_mean)
        np_list = np_mean.tolist()
        col_2 = ['open', 'close', 'low', 'high', 'change']
        stock_dic = dict(zip(col_2, np_list))
        return stock_dic


    def radar_pic(self, file_name):

        stock_dic = self.get_stock_dic(file_name)
        key = list(stock_dic.keys())
        value = list(stock_dic.values())
        # 标签
        labels = np.array(key)
        # 数据个数
        dataLenth = 5
        # 数据
        data = np.array(value)
        angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)
    
        data = np.concatenate((data, [data[0]]))
        angles = np.concatenate((angles, [angles[0]]))
    
        fig = plt.figure()

        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, data, 'ro-', linewidth=2)
        ax.set_thetagrids(angles * 180 / np.pi, labels, fontproperties="SimHei")
        ax.set_title("radar", va='bottom', fontproperties="SimHei")
        ax.grid(True)

        plt.savefig('static/img/analysis/'+"analysis_"+file_name+'.png')
        #plt.show()


# if __name__ == '__main__':
#     ra = radar_pic()
#     dic = ra.radar_pic('000002.SZ.CSV')