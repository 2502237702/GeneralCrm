# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 16:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': '学员账号总览', 'verbose_name_plural': '学员账号总览'},
        ),
    ]
