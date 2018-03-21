#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 22:30
# @Author  : LiuShaoheng


from django.conf import settings
import os

settings.TEMPLATES[0]['DIRS'] += [os.path.join(settings.BASE_DIR, 'kingadmin/templates')]

settings.STATICFILES_DIRS += [os.path.join(settings.BASE_DIR, 'kingadmin/static')]

print(settings.STATICFILES_DIRS)








