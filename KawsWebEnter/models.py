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


# 测试计划数据库模型
class TestPlanVersion(models.Model):
    id = models.IntegerField(primary_key=True)
    targetversion = models.FloatField(max_length=20,blank=True,null=False)
    versionplan = models.CharField(max_length=4000,blank=True,null=True)
    creattime = models.DateField(auto_now_add=True,auto_now=False)
    def __str__(self):
         return self.targetversion


# 测试员用户表（待拓展）
class Testuser(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'testuser'

#首页介绍测试平台内容存表，保证测试平台介绍和链接可以通过数据库实时改变
class TestPlatformIntroduce(models.Model):
    id = models.IntegerField(primary_key=True)
    platformname = models.CharField(max_length=50,blank=True,null=False)
    platformintroduce = models.CharField(max_length=255,blank=True,null=True)
    Urllink = models.CharField(max_length=50,blank=True,null=False)
    def __str__(self):
         return self.platformname

# 用例版本展示列表
class TestCaseVersionDisplay(models.Model):
    id = models.IntegerField(primary_key=True)
    versionname = models.CharField(max_length=30,blank=True,null=True)
    versionintroduce = models.CharField(max_length=255,blank=True,null=True)
    testlinkurl = models.CharField(max_length=255,blank=True,null=True)
    author = models.CharField(max_length=20,blank=True,null=True)
