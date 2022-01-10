from django.contrib import admin
from .models import Navbar
# Register your models here.

class NavbarAdmin(admin.ModelAdmin):
    model = Navbar
    list_display = ("name","url_name","active")

admin.site.register(Navbar,NavbarAdmin)