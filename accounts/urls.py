# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
from accounts import views
from django.conf.urls import url
urlpatterns = [
    url(r'^add/$', views.add),
    url(r'^delete/$', views.delete),
    url(r'^change/$', views.change),
    url(r'^select/$', views.select),
]
