#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 22:17
# @Author  : LiuShaoheng


from django import conf

for app in conf.settings.INSTALLED_APPS:
    try:
        admin_module = __import__("%s.kingadmin" % app)
    except ImportError:
        pass









