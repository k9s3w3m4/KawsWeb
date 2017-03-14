# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


#定义一个存储全部测试用网址的模型，以后所有网址从这个模型中获取
class BaseUrlForTest(models.Model):
    id = models.IntegerField(primary_key=True)
    webname = models.CharField(max_length=40,blank=True,null=True)
    weburl=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.webname

class Testuser(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'testuser'