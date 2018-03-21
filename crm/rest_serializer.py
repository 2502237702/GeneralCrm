#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 11:37
# @Author  : LiuShaoheng


from crm import models
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        depth = 2
        fields = ('url', 'name', 'email', 'is_staff', 'is_superuser', 'roles')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = ('name',)










