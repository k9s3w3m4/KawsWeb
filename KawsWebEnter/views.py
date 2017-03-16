from django.shortcuts import render
from django.http import HttpResponse
from .models import Testuser
from .models import BaseUrlForTest
from .models import TestPlanVersion
from .models import TestPlatformIntroduce
from django.template import RequestContext,loader

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

def tutorial(request):
    return HttpResponse(u"教程跳转测试")

