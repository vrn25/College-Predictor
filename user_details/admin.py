from django.contrib import admin
from . models import FillProfile
from .models import FillPrefer,GiveResult
# Register your models here.

admin.site.register(FillProfile)
admin.site.register(FillPrefer)
admin.site.register(GiveResult)