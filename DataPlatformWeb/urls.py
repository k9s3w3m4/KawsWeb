from django.conf.urls import url
from . import views
urlpatterns = [
   url(r'^changemobile/$',views.ChangeMobile,name='Changemobile')
]
