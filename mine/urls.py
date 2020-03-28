# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
from mine import views
from django.conf.urls import url
urlpatterns = [
    url(r'^cart_add/$', views.cart_add),
    url(r'^cart_delete/$', views.cart_delete),
    url(r'^cart_change/$', views.cart_change),
    url(r'^cart_select/$', views.cart_select),
    url(r'^order_add/$', views.order_add),
    url(r'^order_delete/$', views.order_delete),
    url(r'^order_change/$', views.order_change),
    url(r'^order_select/$', views.order_select),
]
