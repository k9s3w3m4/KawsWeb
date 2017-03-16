from django.conf.urls import url
from . import views
urlpatterns = [
     url(r'^$', views.index,name='index'),
     url(r'^index2/$', views.index2,name='index2'),
     url(r'^testlinkjump/$', views.testlinkjump,name='testlinkjump'),
     url(r'^urljump/$', views.UrlBaseJump,name='UrlBaseJump'),
     url(r'^tutorial/$',views.tutorial,name='tutorial')
]
