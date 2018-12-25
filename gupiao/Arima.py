import datetime
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.arima_model import ARIMA
# Create your tests here.
class ArimaTest:
# ARIMA 模型函数 历史数据查询
    def history(self,filename):
        ts_simu200= pd.read_csv(filename,index_col='t')
        ts_simu200.head()
        dates=pd.date_range(start='2017/01/01', periods=200)
        ts_simu200.set_index(dates, inplace=True)
        dta=ts_simu200['ARIMA']
        ts_simu200.head()
        dta
        ts_simu200.plot(figsize=(20,10))
        plt.savefig('./static/img/arimahistory.png')
        #plt.show()

# ARIMA 模型函数 股票预测
    def forecast(self,filename):
        ts_simu200 = pd.read_csv(filename, index_col='t')
        ts_simu200.head()

        dates = pd.date_range(start='2017/01/01', periods=200)
        ts_simu200.set_index(dates, inplace=True)
        dta = ts_simu200['ARIMA']

        ts_simu200.head()

        dta

        # 平稳性检验
        result = ADF(dta)
        print('ADF Statistic: %f' % result[0])
        print('p-value: %f' % result[1])

        diff1 = dta.diff(1)
        diff1.dropna(inplace=True)

        (p, q) = (sm.tsa.arma_order_select_ic(diff1, max_ar=3, max_ma=3, ic='aic')['aic_min_order'])
        print(p, q)
        arima110 = sm.tsa.ARIMA(dta, (1, 1, 0)).fit()
        resid = arima110.resid  # 残差

        # fig = arima110.plot_predict('20170102',
        #                         '20170820',
        #                             dynamic=False, plot_insample=True)
        fig = arima110.plot_predict(pd.to_datetime('2017-01-02'),
                                    pd.to_datetime('2017-01-01') + datetime.timedelta(days=len(ts_simu200) + 10),
                                    dynamic=False, plot_insample=True)
        fig.set_figwidth(15)
        fig.set_figheight(8)
        plt.savefig('./static/img/arimaforecast.png')