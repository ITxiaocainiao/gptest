# -*- coding: utf-8 -*-

import pandas as pd
#预处理
def pre_treatment_1(csv_name):
    #读取csv文件并转换成utf-8编码
    df_1 = pd.read_csv(csv_name, encoding='gbk')
    df_1.to_csv('data_complete/' + csv_name, encoding='utf-8')
    df_1 = pd.read_csv('data_complete/' + csv_name, encoding='utf-8')
    #获取列字列表
    col_1 = df_1.columns.values.tolist()
    #删除全为na的列
    col_1.remove('B股流通市值(元)')
    col_1.remove('B股流通股本(股)')
    col_1.remove('市盈率')
    col_1.remove('市净率')
    col_1.remove('市销率')
    col_1.remove('市现率')
    col_1.remove('Unnamed: 0')
    col_1.remove('Unnamed: 24')
    #生成新dataframe
    df_1 = df_1[col_1]
    #删去含有na的行并存储新的csv文件
    df_1 = df_1.dropna(axis=0,how='any')
    df_1.to_csv('data_complete/' + csv_name, encoding='utf-8')
    print(df_1.loc[:, '简称']+'\t'+str(df_1.shape[1]))


    df_1 = pd.read_csv('data_complete/' + csv_name, encoding='utf-8')
    #将第二天的最高值最为label列添加进文件
    max = df_1['最高价(元)'].tolist()
    max = max[1:]
    #去除数据中第一天数据
    df_2 = df_1.drop([df_1.shape[0]-1], axis=0)
    #添加label列
    df_2['label'] = max
    # 去除多余列
    col_2 = df_2.columns.values.tolist()
    col_2.remove('Unnamed: 0')
    #生成对应LSTM-master中stock_predict_2中所用数据样式
    col_new = ['代码', '日期', '开盘价(元)', '收盘价(元)', '最低价(元)',
            '最高价(元)', '总股本(股)', '总市值(元)', '涨跌幅(%)', 'label']
    df_2 = df_2[col_new]
    df_2.to_csv('data_complete/' + csv_name, encoding='utf-8')



if __name__ == '__main__':
    pre_treatment_1('000002.SZ.CSV')
    pre_treatment_1('000004.SZ.CSV')
    pre_treatment_1('000005.SZ.CSV')
    pre_treatment_1('000006.SZ.CSV')
    pre_treatment_1('000007.SZ.CSV')
    pre_treatment_1('000008.SZ.CSV')
    pre_treatment_1('000009.SZ.CSV')
    pre_treatment_1('000010.SZ.CSV')




