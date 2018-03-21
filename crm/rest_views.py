#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 11:41
# @Author  : LiuShaoheng


from rest_framework import viewsets
from crm.rest_serializer import UserSerializer, RoleSerializer
from crm import models


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = RoleSerializer











