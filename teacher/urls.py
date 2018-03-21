#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 22:49
# @Author  : LiuShaoheng


from django.conf.urls import url
from teacher import views

urlpatterns = [
    url(r'^$', views.dashboard, name="teacher_dashboard"),
    url(r'^my_classes/$', views.my_classes, name="my_classes"),
    url(r'^my_classes/(\d+)/stu_list/$', views.view_class_stu_list, name="view_class_stu_list"),

]












