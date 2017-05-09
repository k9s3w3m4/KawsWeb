from django.shortcuts import render
from django.http import HttpResponse
from .models import Testuser
from .models import BaseUrlForTest
from .models import TestPlanVersion
from .models import TestPlatformIntroduce
from .models import TestCaseVersionDisplay
from .models import TbUser
from .models import *
from .models import MoblieStatus
from django.template import RequestContext,loader
# 首页从数据库取值传值
def index(request):
    Testplanlist = TestPlanVersion.objects.order_by('-id')
    Testplatformintroducelist= TestPlatformIntroduce.objects.order_by('id')
    template = loader.get_template('enter/index.html')
    context = RequestContext(request,{'Testplanlist':Testplanlist,'Testplatformintroducelist':Testplatformintroducelist})
    return HttpResponse(template.render(context))


def index2(request):
    namelist=Testuser.objects.order_by('name')
    output='/n '.join([p.name for p in namelist] )
    return HttpResponse(output)

def index3(request):
    phone_name_list = Testuser.objects.order_by('id')[:5]
    template=loader.get_template('enter/index3.html')
    context=RequestContext(request,{'phone_name_list':phone_name_list})
    return HttpResponse(template.render(context))


def testlinkjump(request):
    jumpstring = '跳转到testlink'
    template=loader.get_template('enter/testlinkjump.html')
    contextt=RequestContext(request,jumpstring)
    return  HttpResponse(template.render(contextt))


def UrlBaseJump(request):
    webname_url_list = BaseUrlForTest.objects.order_by('id')[:10]
    TbUser_list = TbUser.objects.using('stagedb').filter(username = 'xcx')
    template=loader.get_template('enter/BaseUrlJump.html')
    context = RequestContext(request,{'webname_url_list':webname_url_list,'TbUser_list':TbUser_list})
    return HttpResponse(template.render(context))

# 教程部分待拓展，现在只是简单放了个测试
def tutorial(request):
    return HttpResponse(u"教程跳转测试")

def TestCasePlatform(request):
    testcaseversiondisplaylist = TestCaseVersionDisplay.objects.order_by('id')
    template = loader.get_template('enter/TestCasePlatform.html')
    context = RequestContext(request,{'testcaseversiondisplaylist':testcaseversiondisplaylist})
    return HttpResponse(template.render(context))

def DataPlatform(request):
    template = loader.get_template('enter/DataPlatform.html')
    context = RequestContext(request)
    return  HttpResponse(template.render(context))

# 自动化测试页
def AutoTestPlatform(request):
    template = loader.get_template('enter/AutoTestPlatform.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


# BUG管理页
def BUGManagePlatform(request):
    template = loader.get_template('enter/BUGManagePlatform.html')
    context = RequestContext(request)
    return  HttpResponse(template.render(context))


# app打包页
def AppPackagePlatform(request):
    templte = loader.get_template('enter/AppPackagePlatform.html')
    context = RequestContext(request)
    return HttpResponse(templte.render(context))


# 报告管理页
def ReportManagePLatform(request):
    ReportWebList = BaseUrlForTest.objects.filter(webname__contains='报告')
    template = loader.get_template('enter/ReportManagePlatform.html')
    context = RequestContext(request,{'ReportWebList':ReportWebList})
    return HttpResponse(template.render(context))


#  真机使用状态页
def ShowMoblieStatus(request):
    MobileStatusList = MoblieStatus.objects.order_by('id')
    context = {'mobilestatuslist':MobileStatusList}
    return render(request,'enter/MobleStatusManagePlatform.html',context)


# 申请使用手机
def UseMobile(request):
    getmobileid = request.GET['mobileid']
    mobile_list = MoblieStatus.objects.get(id = getmobileid)
    user_list = Testuser.objects.order_by('id')
    context= {'mobilelist':mobile_list,'userlist':user_list}
    return  render(request,'enter/UseMobile.html',context)

# 申请使用完成
def UseMobileComplete(request):
    getmobileid = request.POST['mobileid']
    getreturntime = request.POST['returntime']
    getmobilestatus = request.POST['mobilestatus']
    getsystemversion = request.POST['systemversion']
    getuserid = request.POST['user']
    mobilelist = MoblieStatus.objects.get(id = getmobileid)
    userlist = Testuser.objects.get(id =getuserid)
    mobilelist.user.clear()
    mobilelist.user.add(userlist)
    mobilelist.mobilestatus=getmobilestatus
    mobilelist.returntime = getreturntime
    mobilelist.systemversion = getsystemversion
    mobilelist.save()
    return render(request,'enter/UseMobileComplete.html')
