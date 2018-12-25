from django.conf.urls import url
from gupiao import views
urlpatterns = [
    url(r'^index$', views.index, name='index'), #首页
    url(r'^forecast$', views.forecast, name='forecast'), #预测页面
    url(r'^analysis$', views.analysis, name='analysis'), #分析页面
    url(r'^demo$', views.demo, name='demo'),
]
