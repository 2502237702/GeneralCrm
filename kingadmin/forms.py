#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 22:24
# @Author  : LiuShaoheng


from django.forms import ModelForm
from django import forms


def __new__(cls, *args, **kwargs):

    for field_name in cls.base_fields:
        field = cls.base_fields[field_name]

        attr_dic = {'placeholder': field.help_text}
        if 'BooleanField' not in field.__repr__():
            attr_dic.update({'class': 'form-control'})

            if 'ModelChoiceField' in field.__repr__():
                attr_dic.update({'data-tag':field_name})

        if cls.Meta.form_create is False:
            if field_name in cls.Meta.admin.readonly_fields:
                attr_dic['disabled'] = True

        field.widget.attrs.update(attr_dic)

        if hasattr(cls.Meta.model,"clean_%s" % field_name):
            clean_field_func = getattr(cls.Meta.model,"clean_%s" % field_name)
            setattr(cls,"clean_%s" % field_name,clean_field_func)
    else:
        if hasattr(cls.Meta.model, "clean2"):
            clean_func = getattr(cls.Meta.model, "clean")
            setattr(cls, "clean", clean_func)
        else:
            setattr(cls, "clean", default_clean)

    return ModelForm.__new__(cls)


def default_clean(self):
    '''form defautl clean method'''

    # print("cleaned_dtat:",self.cleaned_data)

    if self.Meta.admin.readonly_table is True:
        raise forms.ValidationError(("This is a readonly table!"))
    if self.errors:
        raise forms.ValidationError(("Please fix errors before re-submit."))
    if self.instance.id is not None:
        for field in self.Meta.admin.readonly_fields:
            old_field_val = getattr(self.instance,field)
            form_val = self.cleaned_data.get(field)
            print("filed differ compare:",old_field_val,form_val)
            if old_field_val != form_val:
                if self.Meta.partial_update:
                    if field not in self.cleaned_data:
                        continue

                self.add_error(field,"Readonly Field: field should be '{value}' ,not '{new_value}' ".format(**{'value':old_field_val,'new_value':form_val}))


def create_form(model,fields,admin_class,form_create=False,**kwargs):
    class Meta:
        model = admin_class.model
        fields = '__all__'
    # setattr(Meta,'model',model)
    # setattr(Meta,'fields',fields)
    setattr(Meta,'admin',admin_class)
    setattr(Meta,'form_create',form_create)
    setattr(Meta,'partial_update',kwargs.get("partial_update"))

    attrs = {'Meta':Meta}
    name = 'DynamicModelForm'
    model_form = type(name, (ModelForm,), attrs)
    setattr(model_form,'__new__',__new__)
    if kwargs.get("request"):
        setattr(model_form,'_request',kwargs.get("request"))
    return model_form




