# gptest 
# 多模型在线股票预测系统。http://118.24.60.118:8000/gupiao/index
本系统主要使用LSTM递归神经网络算法和SVM算法进行股票价格的预测，同时提供了股票历史数据查询和股票诊断分析功能。查询，预测以及分析的结果均以图表的形式呈现。该系统中提供了多支不同股票的历史数据，基于这些历史数据实现股票价格的预测，以及股票诊断分析等功能。
# 数据分析
数据来源：http://dataju.cn/Dataju/web/datasetInstanceDetail/38
深证证券交易所A股股票日线数据，1766支股票，时间区间为 1999.12.09 至 2016.06.08，前复权，剔除假期休市。
  名称  数据类型  数据格式
  
  1	股票代码	string	文本字符串格式
  
  2	股票名称简称	string	文本字符串格式
  
  3	成交量(股)	int	普通整数格式
  
  4	前收盘价(元)	float	普通浮点数格式
  
  5	开盘价(元)	float	普通浮点数格式
  
  6	最高价(元)	float	普通浮点数格式
  
  7	最低价(元)	float	普通浮点数格式
  
  8	收盘价(元)	float	普通浮点数格式
  
  9	成交金额(元)	float	普通浮点数格式
  
  10	涨跌(元)	float	普通浮点数格式
  
  11	涨跌幅(%)	float	普通浮点数格式
  
  12	换手率(%)	float	普通浮点数格式
  
  13	A股流通市值(元)	float	普通浮点数格式
  
  14	市盈率	float	普通浮点数格式
  
  15	市净率	float	普通浮点数格式
  
  16	市销率	float	普通浮点数格式
  
  17	市现率	float	普通浮点数格式
  
  18	日期时间	string	时间格式 YYYY/MM/dd



# 项目搭建
1.项目运行环境：本系统运行环境python版本为python3.5.2（建议python3.5或者python3.6） 前端使用django框架进行搭建，django版本为1.8.19（建议不要使用最新版本）关于python环境的安装和配置以及django框架的安装配置和使用方法这里不再详细描述，如果需要请参考：https://www.cnblogs.com/lovele-/p/8718894.html

2.算法所依赖的包
为了能够正常运行代码，需要在python中安装算法所依赖的包。在Windows系统下建议使用python强大的包管理工具pip 

（例如安装TensorFlow，可以在Windows命令行下面直接输入：pip install tensorflow 等待安装即可。）需要安装的包有：padas,numpy,tensorflow,matplotlib,statsmodels,scipy,patsy,sklearn。

所有的包安装成功之后，可以使用 pip list 命令进行查看。

3.使用方法
本地部署：

使用开发工具pycharm：（注意要用专业版），前提要有github账号，本地安装git并在pycharm中登录github账号以及配置好git。可以直接克隆到pycharm中，然后在pycharm终端中输入 python manage.py runserver 开启服务器，在浏览器中输入127.0.0.1:8000/gupiao/index 即可访问系统。

不使用开发工具运行系统方法：可以下载压缩包，然后解压，Windows系统下进入命令行，同样通过 python manag.py runserver 开启服务器，浏览器访问即可。

云服务器部署：(Windows系统) 云服务器中要安装好python，django以及开发依赖的包等，同本地安装一样。把项目源文件拷贝到云服务器中，在系统命令行输入 (注意是：python manage.py runserver 0.0.0.0:8000) 开启服务器，然后通过浏览器进行访问即可。访问方式：云服务器公网ip:8000/gupiao/index

# 可能会遇到的坑

1.把项目部署在云服务器上时如果遇到拒绝访问的解决办法：（1）在云服务器安全组设置中添加可以访问的端口。（2）修改setting.py文件中的ALLOWED_HOSTS[]为ALLOWED_HOSTS['*']     (3) 开启服务器时一定要使用 python manage.py runserver 0.0.0.0:8000

2.使用plt.savefig()来保存生成的图像时要写在plt.show()的前面，不然保存的图像是空白的。

# 项目扩展
本系统中在股票价格预测模块目前主要实现了基于LSTM递归神经网络算法和SVM算法的预测，如果读者有更好的预测算法可以进行扩展。在项目分析诊断模块，目前该系统只实现了基于LSTM递归神经网络算法的诊断分析，如果读者有更多更好的实现算法，可以尝试进行拓展。
