# gptest 
# 多模型在线股票预测系统。
本系统主要使用LSTM递归神经网络算法和SVM算法进行股票价格的预测，同时提供了股票历史数据查询和股票诊断分析功能。查询，预测以及分析的结果均以图表的形式呈现。该系统中提供了多支不同股票的历史数据，基于这些历史数据实现股票价格的预测，以及股票诊断分析等功能。
# 数据分析

# 项目搭建
1.项目运行环境：本系统运行环境python版本为python3.5.2（建议python3.5或者python3.6） 前端使用django框架进行搭建，django版本为1.8.19（建议不要使用最新版本）关于python环境的安装和配置以及django框架的安装配置和使用方法这里不再详细描述，如果需要请参考：https://www.cnblogs.com/lovele-/p/8718894.html

2.算法所依赖的包
为了能够正常运行代码，需要在python中安装算法所依赖的包。在Windows系统下建议使用python强大的包管理工具pip （例如安装TensorFlow，可以直接在Windows命令行下面直接输入：pip install tensorflow 等待安装即可。）需要安装的包有：padas,numpy,tensorflow,matplotlib,statsmodels,scipy,patsy,sklearn。所有的包安装成功之后，可以使用 pip list 命令进行查看。

3.使用方法
# 可能会遇到的坑

# 项目扩展
