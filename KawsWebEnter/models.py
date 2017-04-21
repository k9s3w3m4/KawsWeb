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
    def __float__(self):
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



#在模型中定义tbUser表
class TbUser(models.Model):
    userkey = models.CharField(primary_key=True, max_length=64)
    mobile = models.CharField(max_length=66, blank=True, null=True)
    username = models.CharField(max_length=64)
    imageurl = models.CharField(max_length=256, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    sickkindsid = models.CharField(max_length=32, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    sickdate = models.DateField(blank=True, null=True)
    area = models.CharField(max_length=32, blank=True, null=True)
    departments = models.CharField(max_length=32, blank=True, null=True)
    hospital = models.CharField(max_length=50, blank=True, null=True)
    sickdegree = models.CharField(max_length=16, blank=True, null=True)
    regtime = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    orgtype = models.CharField(max_length=1, blank=True, null=True)
    userid = models.CharField(max_length=32, blank=True, null=True)
    quenotice = models.IntegerField(blank=True, null=True)
    commentnotice = models.CharField(max_length=1, blank=True, null=True)
    attennotice = models.CharField(max_length=1, blank=True, null=True)
    clienttype = models.CharField(max_length=1, blank=True, null=True)
    channelid = models.CharField(max_length=32, blank=True, null=True)
    relationship = models.CharField(max_length=32, blank=True, null=True)
    registwhy = models.CharField(max_length=32, blank=True, null=True)
    usestatus = models.IntegerField(blank=True, null=True)
    medicalrecord = models.CharField(max_length=1, blank=True, null=True)
    keywords = models.IntegerField(blank=True, null=True)
    doctordegree = models.CharField(max_length=1, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    praisenum = models.CharField(db_column='praiseNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    joinactive = models.CharField(max_length=1, blank=True, null=True)
    invitationcode = models.CharField(max_length=30, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    sectype = models.CharField(max_length=2, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    commentnum = models.CharField(db_column='commentNUM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=20, blank=True, null=True)
    has_set_diseased_state = models.IntegerField(blank=True, null=True)
    latest_checked_in_at = models.DateTimeField(blank=True, null=True)
    has_mood_note_notice = models.IntegerField(blank=True, null=True)
    has_community_notice = models.IntegerField(blank=True, null=True)
    has_doctor_comment_notice = models.IntegerField(blank=True, null=True)
    has_apply_doctor_notice = models.IntegerField(blank=True, null=True)
    has_message_notice = models.IntegerField(blank=True, null=True)
    has_followed_notice = models.IntegerField(blank=True, null=True)
    modified_username_at = models.DateTimeField(blank=True, null=True)
    old_name = models.CharField(max_length=255, blank=True, null=True)
    sign = models.CharField(max_length=255, blank=True, null=True)
    money = models.CharField(max_length=255, blank=True, null=True)
    doctorvideo = models.CharField(max_length=255, blank=True, null=True)
    wx_open_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tb_user'
#    真机使用状态表
class MoblieStatus(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    mobliename = models.CharField(max_length=255)
    mobilestatus = models.IntegerField(default=1)
    user = models.ManyToManyField(Testuser)
    lendtime = models.DateField(auto_created=True,auto_now_add=True)
    returntime = models.DateField(auto_created=True,auto_now_add=True)
    def __str__(self):
        return self.mobliename
