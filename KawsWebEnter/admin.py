from django.contrib import admin
from .models import Testuser
from .models import BaseUrlForTest
from .models import TestPlanVersion
from .models import TestPlatformIntroduce
from .models import TestCaseVersionDisplay
admin.site.register(Testuser)
admin.site.register(BaseUrlForTest)
admin.site.register(TestPlanVersion)
admin.site.register(TestPlatformIntroduce)
admin.site.register(TestCaseVersionDisplay)