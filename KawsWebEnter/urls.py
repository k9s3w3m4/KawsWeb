from django.conf.urls import url
from . import views
urlpatterns = [
     url(r'^$', views.index,name='index'),
#     url(r'^(?P<id>[0-9]+)/$',views.idshow,name='idshow'),
#     url(r'^(?P<name>[0-9]+)/nameshow',views.nameshow,name='nameshow'),
#     url(r'^(?P<id>[0-9]+)/phoneshow',views.phone,name='phone'),
     url(r'^index2/$', views.index2,name='index2'),
     url(r'^index3/$', views.index3,name='index3'),
     url(r'^testlinkjump/$', views.testlinkjump,name='testlinkjump'),
     url(r'^urljump/$', views.UrlBaseJump,name='UrlBaseJump'),
]
