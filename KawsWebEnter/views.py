from django.shortcuts import render
from django.http import HttpResponse
from .models import Testuser
from .models import BaseUrlForTest
from .models import TestPlanVersion
from .models import TestPlatformIntroduce
from .models import TestCaseVersionDisplay
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
    template=loader.get_template('enter/BaseUrlJump.html')
    context = RequestContext(request,{'webname_url_list':webname_url_list})
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


def AutoTestPlatform(request):
    template = loader.get_template('enter/AutoTestPlatform.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def BUGManagePlatform(request):
    template = loader.get_template('enter/BUGManagePlatform.html')
    context = RequestContext(request)
    return  HttpResponse(template.render(context))