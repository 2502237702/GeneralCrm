#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 22:26
# @Author  : LiuShaoheng


from kingadmin import custom_perm_logic

# 权限样式 app_权限名字

perm_dic = {
    'crm_table_index':['table_index','GET',[],{},],
    'crm_app_tables':['app_tables','GET',[],{},],
    'crm_customers':['customers','GET',[],{},],
    'crm_table_list':['table_list','GET',[],{}],
    'crm_table_list_action':['table_list','POST',["admin_action",],{}],
    'crm_table_list_view':['table_change','GET',[],{}],
    'crm_table_list_change':['table_change','POST',[],{}],
    'crm_table_add_view':['table_add','GET',[],{}],
    'crm_table_add_add':['table_add','POST',[],{}],
    'crm_table_del_view':['table_del','GET',[],{}],
    'crm_table_del_del':['table_del','POST',[],{}],
    'crm_personal_password_reset_view':['personal_password_reset','GET',[],{}],
    'crm_personal_password_reset':['personal_password_reset','POST',[],{}],
    'crm_password_reset_view':['password_reset','GET',[],{}],
    'crm_password_reset':['password_reset','POST',[],{}],
    'crm_can_access_my_clients':['table_list','GET',[],
                                 {'perm_check':33,'arg2':'test'},
                                 custom_perm_logic.only_view_own_customers],  # 自定义钩子测试失败了...
    # 'web_invoke_admin_action':['table_list','POST',[]],
    # 'web_table_change_page':['table_change','GET',[]],
    # 'web_table_change':['table_change','POST',[]],

}













