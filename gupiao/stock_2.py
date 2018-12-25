#coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
np.seterr(divide='ignore', invalid='ignore')


#lightgbm报错
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

class stock_2(object):

    global data

    #隐层神经元的个数
    rnn_unit = 10
    #隐层层数
    lstm_layers = 2
    input_size = 7
    output_size = 1
    #学习率
    lr = 0.0006

    # ——————————————————定义神经网络变量——————————————————
    # 输入层、输出层权重、偏置、dropout参数
    weights = {
        'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
        'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
    }
    biases = {
        'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
        'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
    }
    keep_prob = tf.placeholder(tf.float32, name='keep_prob')


    #获取训练集
    def get_train_data(self, batch_size=60, time_step=20, train_begin=0, train_end=4500):
        batch_index = []
        global data
        data_train = data[train_begin:train_end]
        #标准化
        normalized_train_data = (data_train-np.mean(data_train, axis=0))/np.std(data_train,axis=0)
        #训练集
        train_x, train_y = [], []
        for i in range(len(normalized_train_data)-time_step):

           if i % batch_size == 0:
               batch_index.append(i)
           x = normalized_train_data[i:i+time_step, :7]
           #增加维度
           y = normalized_train_data[i:i+time_step, 7, np.newaxis]
           train_x.append(x.tolist())
           train_y.append(y.tolist())
        batch_index.append((len(normalized_train_data)-time_step))
        return batch_index, train_x, train_y


    #获取测试集
    def get_test_data(self, time_step=20, test_begin=4500):
        global data
        i = 0
        data_test = data[test_begin:]
        mean = np.mean(data_test, axis=0)
        std = np.std(data_test, axis=0)
        # 标准化
        print(data_test)
        print(mean)
        print(std)
        normalized_test_data = (data_test-mean)/std
        # 有size个sample
        size = (len(normalized_test_data)+time_step-1)//time_step
        test_x, test_y = [], []
        for i in range(size-1):
           x = normalized_test_data[i*time_step:(i+1)*time_step, :7]
           y = normalized_test_data[i*time_step:(i+1)*time_step, 7]
           test_x.append(x.tolist())
           test_y.extend(y)
        test_x.append((normalized_test_data[(i+1)*time_step:, :7]).tolist())
        test_y.extend((normalized_test_data[(i+1)*time_step:, 7]).tolist())
        return mean, std, test_x, test_y


    #——————————————————定义神经网络变量——————————————————
    def lstmCell(self):
        #basicLstm单元
        basicLstm = tf.nn.rnn_cell.BasicLSTMCell(stock_2.rnn_unit)
        # dropout
        drop = tf.nn.rnn_cell.DropoutWrapper(basicLstm, output_keep_prob=stock_2.keep_prob)
        return basicLstm

    def lstm(self, X):
        batch_size = tf.shape(X)[0]
        time_step = tf.shape(X)[1]
        w_in = stock_2.weights['in']
        b_in = stock_2.biases['in']
        # 需要将tensor转成2维进行计算，计算后的结果作为隐藏层的输入
        input = tf.reshape(X, [-1, stock_2.input_size])
        input_rnn = tf.matmul(input, w_in)+b_in
        # 将tensor转成3维，作为lstm cell的输入
        input_rnn = tf.reshape(input_rnn, [-1, time_step, stock_2.rnn_unit])
        cell = tf.nn.rnn_cell.MultiRNNCell([stock_2.lstmCell(self) for i in range(stock_2.lstm_layers)])
        init_state = cell.zero_state(batch_size, dtype=tf.float32)
        output_rnn, final_states = tf.nn.dynamic_rnn(cell, input_rnn, initial_state=init_state, dtype=tf.float32)
        output = tf.reshape(output_rnn, [-1, stock_2.rnn_unit])
        w_out = stock_2.weights['out']
        b_out = stock_2.biases['out']
        pred = tf.matmul(output, w_out)+b_out
        return pred, final_states


    #————————————————训练模型————————————————————
    def train_lstm(self, batch_size=60, time_step=20, train_begin=2000, train_end=4500):
        X = tf.placeholder(tf.float32, shape=[None, time_step, stock_2.input_size])
        Y = tf.placeholder(tf.float32, shape=[None, time_step, stock_2.output_size])
        batch_index, train_x, train_y = stock_2.get_train_data(self, batch_size, time_step, train_begin, train_end)
        with tf.variable_scope("sec_lstm"):
            pred, _ = stock_2.lstm(self, X)
        loss = tf.reduce_mean(tf.square(tf.reshape(pred, [-1])-tf.reshape(Y, [-1])))
        train_op = tf.train.AdamOptimizer(stock_2.lr).minimize(loss)
        saver = tf.train.Saver(tf.global_variables(), max_to_keep=15)

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            # 这个迭代次数，可以更改，越大预测效果会更好，但需要更长时间
            for i in range(20):
                for step in range(len(batch_index)-1):
                    _, loss_ = sess.run([train_op, loss], feed_dict={X: train_x[batch_index[step]:batch_index[step+1]],
                                                                    Y: train_y[batch_index[step]:batch_index[step+1]],
                                                                    stock_2.keep_prob: 0.5})
                print("Number of iterations:", i, " loss:", loss_)
            print("model_save: ", saver.save(sess, 'model_save2/modle.ckpt'))
            #I run the code on windows 10,so use  'model_save2\\modle.ckpt'
            #if you run it on Linux,please use  'model_save2/modle.ckpt'
            print("The train has finished")

    #————————————————预测模型————————————————————
    def prediction(self, time_step=20):

        X = tf.placeholder(tf.float32, shape=[None, time_step, stock_2.input_size])
        mean, std, test_x, test_y = stock_2.get_test_data(self, time_step)
        with tf.variable_scope("sec_lstm", reuse=tf.AUTO_REUSE):
            pred, _ = stock_2.lstm(self, X)
        saver = tf.train.Saver(tf.global_variables())
        with tf.Session() as sess:
            #参数恢复
            module_file = tf.train.latest_checkpoint('model_save2')
            saver.restore(sess, module_file)
            test_predict = []
            for step in range(len(test_x)-1):
              prob = sess.run(pred, feed_dict={X: [test_x[step]], stock_2.keep_prob:1})
              predict = prob.reshape((-1))
              test_predict.extend(predict)
            test_y = np.array(test_y)*std[7]+mean[7]
            test_predict = np.array(test_predict)*std[7]+mean[7]
            # 偏差程度
            acc = np.average(np.abs(test_predict-test_y[:len(test_predict)])/test_y[:len(test_predict)])
            print("The accuracy of this predict:", acc)
            #以折线图表示结果

            # print(len(test_y))
            # print(len(test_predict))

            plt.figure()
            plt.plot(list(range(len(test_predict))), test_predict, color='b',)
            plt.plot(list(range(len(test_y))), test_y,  color='r')
            plt.savefig('static/img/forecast/forecast_02.png')
            plt.show()


    def run(self,file_name):
        # ——————————————————导入数据——————————————————————
        f = open('gupiao/data/data_complete/'+file_name, encoding='utf-8')
        # f=open('dataset_2.csv')
        # 读入股票数据
        df = pd.read_csv(f)
        df.pop("Unnamed: 0")
        print(df)

        # 取第3-11列
        global data
        data = df.iloc[:, 2:10].values
        # data = df.iloc[:, 2:10].values
        #模型训练好后可以注释掉下一条语句
        self.train_lstm()
        self.prediction()



# if __name__ == '__main__':
#     stock = stock_2()
#     stock.run('000002.SZ.CSV')
#     #stock.prediction('000004.SZ.CSV')
