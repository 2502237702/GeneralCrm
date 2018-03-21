from django.db import models
from crm.models import UserProfile,Customer


class Account(models.Model):
    account = models.OneToOneField(UserProfile,related_name="stu_account")
    profile = models.OneToOneField(Customer)

    class Meta:
        verbose_name_plural = '学员账号总览'
        verbose_name = '学员账号总览'




