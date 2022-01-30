from django.contrib import admin
from django.utils.html import format_html

from Market_Product.models import *

# Register your models here.
class ProductImageInline(admin.StackedInline):
    model = Images

class ProductModelAdmin(admin.ModelAdmin):
    list_display    = ['__str__','title','active','image_tag']
    inlines         =[ProductImageInline]

class ReviewAdmin(admin.ModelAdmin):
    list_display    = ['__str__','rate','user','status']

class ColorAdmin(admin.ModelAdmin):
    list_display = ['__str__','color_tag','code']

admin.site.register(Category)
admin.site.register(Product,ProductModelAdmin)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Size)
admin.site.register(Company)
admin.site.register(Color,ColorAdmin)