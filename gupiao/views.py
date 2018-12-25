from django.shortcuts import render, HttpResponse
import json
from gupiao.Arima import ArimaTest
from gupiao.stock_2 import stock_2
from gupiao.radar_pic import radar_pic
from gupiao.svm import svm
from gupiao.stock_history_data import stock_history_data

def index(request):
    ''' 显示主页'''
    if request.method == "POST":
        code = request.POST.get("code")
        ret = {"status": 0, 'url': " "}
        if code == "code02":
            try:
                st = stock_history_data()
                st.stock_data('000002.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 2
        elif code == "code05":
            try:
                st = stock_history_data()
                st.stock_data('000005.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 5
        elif code == "code06":
            try:
                st = stock_history_data()
                st.stock_data('000006.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 6
        elif code == "code07":
            try:
                st = stock_history_data()
                st.stock_data('000007.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 7
        elif code == "code08":
            try:
                st = stock_history_data()
                st.stock_data('000008.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 8
        elif code == "code09":
            try:
                st = stock_history_data()
                st.stock_data('000009.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 9
        elif code == "code10":
            try:
                st = stock_history_data()
                st.stock_data('000010.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 10
        else:
            # 调用ARIMA算法的方法
            ret['status'] = 0
        return HttpResponse(json.dumps(ret))
    return render(request, 'index.html')

def forecast(request):
    '''预测界面'''
    if request.method == "POST":
        code = request.POST.get("code")
        model = request.POST.get("model")
        ret = {"status": 0, 'url': ''}
        if code == "code02" and model == "model01":
            try:
                s = svm()
                s.run('000002.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 12
        elif code == "code05" and model == "model01":
            try:
                s = svm()
                s.run('000005.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 15
        elif code == "code06" and model == "model01":
            try:
                s = svm()
                s.run('000006.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 16
        elif code == "code07" and model == "model01":
            try:
                s = svm()
                s.run('000007.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 17
        elif code == "code09" and model == "model01":
            try:
                s = svm()
                s.run('000009.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 19
        elif code == "code02" and model == "model02":
            try:
                st = stock_2()
                st.run('000002.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 2
        elif code == "code05" and model == "model02":
            try:
                st = stock_2()
                st.run('000005.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 5
        elif code == "code06" and model == "model02":
            try:
                st = stock_2()
                st.run('000006.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 6
        elif code == "code07" and model == "model02":
            try:
                st = stock_2()
                st.run('000007.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 7
        elif code == "code09" and model == "model02":
            try:
                st = stock_2()
                st.run('000009.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 9

        else:
            ret['status'] = 0
        return HttpResponse(json.dumps(ret))
    return render(request, 'forecast.html')
def analysis(request):
    '''显示股票分析界面'''
    if request.method == "POST":
        code = request.POST.get("code")
        ret = {"status": 0, 'stock_data': " "}
        if code == "code02":
            try:
                rd = radar_pic()
                pic = rd.radar_pic('000002.SZ.CSV')
                dic = rd.get_stock_dic('000002.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 2
            ret['stock_data'] = dic
        elif code == "code05":
            try:
                rd = radar_pic()
                pic = rd.radar_pic('000005.SZ.CSV')
                dic = rd.get_stock_dic('000005.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 5
            ret['stock_data'] = dic
        elif code == "code06":
            try:
                rd = radar_pic()
                pic = rd.radar_pic('000006.SZ.CSV')
                dic = rd.get_stock_dic('000006.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 6
            ret['stock_data'] = dic
        elif code == "code07":
            try:
                rd = radar_pic()
                pic = rd.radar_pic('000007.SZ.CSV')
                dic = rd.get_stock_dic('000007.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 7
            ret['stock_data'] = dic
        elif code == "code08":
            try:
                rd = radar_pic()
                pic = rd.radar_pic('000008.SZ.CSV')
                dic = rd.get_stock_dic('000008.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 8
            ret['stock_data'] = dic
        elif code == "code09":
            try:
                rd = radar_pic()
                pic = rd.radar_pic('000009.SZ.CSV')
                dic = rd.get_stock_dic('000009.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 9
            ret['stock_data'] = dic
        elif code == "code10":
            try:
                rd = radar_pic()
                pic = rd.radar_pic('000010.SZ.CSV')
                dic = rd.get_stock_dic('000010.SZ.CSV')
                pass
            except Exception as result:
                print("出现错误 %s" % result)
            ret['status'] = 10
            ret['stock_data'] = dic
        else:
            ret['status'] = 0
        return HttpResponse(json.dumps(ret))
    return render(request, 'analysis.html')

def demo(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        ret = {"status": 0, 'url': ''}
        if user == "admin" and pwd == "123":
            ret['status'] = 1
            ret['url'] = '/gupiao/demo'
            arimatest = ArimaTest()
            arimatest.forecast('data2.csv')
        return HttpResponse(json.dumps(ret))

    return render(request, "demo.html")