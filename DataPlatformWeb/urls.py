from django.conf.urls import url
from . import views
urlpatterns = [
   url(r'^changemobile/$',views.ChangeMobile,name='changemobile'),
   url(r'^changeview/$',views.ChangeMobileView,name='changemobileview'),
   url(r'^changecompelet/$',views.ChangeMobileCompelet,name='changecompelet'),
   url(r'^changecontribute/$', views.ChangeContribute, name='changecontribute'),
   url(r'^changecontributeview/$', views.ChangeContributeview, name='changecontributeview'),
   url(r'^changecontributecompelet/$', views.ChangeContibuteComplete, name='changecontributecompelet')
]
