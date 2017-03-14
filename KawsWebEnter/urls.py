from django.conf.urls import url
from . import views
urlpatterns = [
     url(r'^$', views.index,name='index'),
     # url(r'^images/(?p<path>.*)','Django.views.static.serve',{'document_root':'~/PycharmProjects/KawsWeb/KawsWebEnter/images'}),
     url(r'^index2/$', views.index2,name='index2'),
     url(r'^index3/$', views.index3,name='index3'),
     url(r'^testlinkjump/$', views.testlinkjump,name='testlinkjump'),
     url(r'^urljump/$', views.UrlBaseJump,name='UrlBaseJump'),
]
