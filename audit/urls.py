#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 22:50
# @Author  : LiuShaoheng


from django.conf.urls import url
from audit import views


urlpatterns = [

    url(r'^my_application/$', views.my_application,name='my_application'),
    url(r'^flow_detail/(\d+)/$', views.flow_detail,name='flow_detail'),
    url(r'^my_approvals/$', views.my_approvals,name='my_approvals'),
    url(r'^my_approval_records/$', views.my_approval_records,name='my_approval_records'),
    url(r'^flow_examination/(\d+)/$', views.flow_examination,name='flow_examination'),

]










