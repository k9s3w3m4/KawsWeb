"""KawsWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from KawsWebEnter import  views
from DataPlatformWeb import views as dataplatformview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^enter/', include('KawsWebEnter.urls')),
    url(r'^index3/$', views.index3, name='index3'),
    url(r'^dataplatformchange/',include('DataPlatformWeb.urls',namespace='datachange')),
    url(r'^testcaseplatform/$',views.TestCasePlatform,name='testcaseplatform'),
    url(r'^dataplatform/$',views.DataPlatform,name='dataplatform'),
    url(r'^autotestplatform/$', views.AutoTestPlatform, name='autotestplatform'),
    url(r'^bugmanageplatform/$', views.BUGManagePlatform, name='bugmanageplatform'),
    url(r'^apppackageplatform/$',views.AppPackagePlatform,name='apppackageplaform'),
    url(r'^reportmanageplatform/$',views.ReportManagePLatform,name='reportmanageplatform'),
    url(r'^mobilestatus/$',views.ShowMoblieStatus,name='mobilesstatus'),
    url(r'^usemobile/$',views.UseMobile,name='usemobile'),
    url(r'^usemobilecomlete',views.UseMobileComplete,name='usemobilecomplete'),
    url(r'^apppakagemanagement/$',views.APPPakage,name='apppakagemanament')
]
