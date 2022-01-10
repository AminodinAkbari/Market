from django.contrib import admin
from .models import *
# Register your models here.
class OFFBannersadmin(admin.ModelAdmin):
    list_display = ['title','active']

    class Meta:
        Model = HeaderBanner

class OFFLimitTimeadmin(admin.ModelAdmin):
    list_display = ['title','active']

    class Meta:
        Model = HeaderBanner

admin.site.register(HeaderBanner,OFFBannersadmin)
admin.site.register(OFFProduct_limit_time,OFFLimitTimeadmin)