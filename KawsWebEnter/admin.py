from django.contrib import admin
from .models import *
admin.site.register(Testuser)
admin.site.register(BaseUrlForTest)
admin.site.register(TestPlanVersion)
admin.site.register(TestPlatformIntroduce)
admin.site.register(TestCaseVersionDisplay)
class MobileStatusAdmin(admin.ModelAdmin):
    fields = ('mobliename','mobilestatus','user','systemversion')
admin.site.register(MoblieStatus,MobileStatusAdmin)
# admin.site.register(MoblieStatus)