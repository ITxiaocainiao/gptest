import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler


class svm (object):

    def run(self, file_name):

        data = pd.read_csv('gupiao/data/data_complete/'+file_name)
        data = data.drop(['代码', '日期'], axis=1)

        n = len(data)
        train_n = int(n * 0.8)

        X_train = data.iloc[:train_n, :-1]
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        y_train = data.iloc[:train_n, -1]

        X_test = data.iloc[train_n:, :-1]
        X_test = scaler.fit_transform(X_test)
        y_test = data.iloc[train_n:, -1]

        svr_rbf = SVR(kernel='rbf', C=1, gamma=1)
        svr_rbf.fit(X_train, y_train)
        # y_pred = svr_rbf.predict (X_train)
        y_pred = svr_rbf.predict(X_test)
        plt.figure()
        # plt.plot(range(len(X_train)), y_train, label='data', color='green', linestyle='-')
        plt.plot(range(len(X_test)), y_test, label='train_data', color='green', linestyle='-')
        # plt.plot(range(len(X_train)), y_pred, label='data', color='red', linestyle='--')
        plt.plot(range(len(X_test)), y_pred, label='predict_data', color='red', linestyle='--')
        plt.legend()
        png_name = 'static/img/forecast/'+'forecast_'+file_name+'.png'
        plt.savefig(png_name)
        #plt.show()
#
# if __name__ == '__main__':
#      svm = svm()
#      svm.run('000006.SZ.CSV')
