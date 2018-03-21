#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 22:14
# @Author  : LiuShaoheng


from django.shortcuts import render, redirect


class BaseKingAdmin(object):
    list_display = []
    list_filters = []
    search_fields = []
    list_per_page = 20
    ordering = None
    filter_horizontal = []
    list_editable = []
    readonly_fields = []
    actions = ["delete_selected_objs", ]
    readonly_table = False
    modelform_exclude_fields = []
    add_form = None

    def delete_selected_objs(self, request, querysets):
        app_name = self.model._meta.app_label
        model_name = self.model._meta.model_name
        if self.readonly_table:
            errors = {"readonly_table": "This table is readonly ,cannot be deleted or modified!"}
        else:
            errors = {}
        if request.POST.get("_delete_confirm") == "yes":
            if not self.readonly_table:
                querysets.delete()
            return redirect("/kingadmin/%s/%s/" % (app_name, model_name))
        selected_ids = ','.join([str(i.id) for i in querysets])
        return render(request, "kingadmin/table_objs_delete.html", {
            "objs": querysets,
            "admin_class": self,
            "app_name": app_name,
            "model_name": model_name,
            "model_verbose_name": self.model._meta.verbose_name,
            "selected_ids": selected_ids,
            "admin_action": request._admin_action,
            "errors": errors
        })

    def default_form_validation(self):
        '''用户可以在此进行自定义的表单验证，相当于django form的clean方法'''
        pass


class AdminAlreadyRegistered(Exception):
    def __init__(self, msg):
        self.message = msg


class AdminSite(object):
    def __init__(self):
        self.enabled_admins = {}

    def register(self, model_class, admin_class=None):

        app_name = model_class._meta.app_label
        model_name = model_class._meta.model_name
        print(app_name, model_name)
        if app_name not in self.enabled_admins:
            self.enabled_admins[app_name] = {}

        if not admin_class:
            admin_class = BaseKingAdmin()
        admin_class.model = model_class

        self.enabled_admins[app_name][model_name] = admin_class


site = AdminSite()
















