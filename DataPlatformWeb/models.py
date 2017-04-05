from __future__ import unicode_literals
from django.db import models
#创建Tbuser模型
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

class TbUserContribution(models.Model):
    userkey = models.CharField(max_length=32, blank=True, null=True)
    contributioinvalue = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    grand_total = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'tb_user_contribution'