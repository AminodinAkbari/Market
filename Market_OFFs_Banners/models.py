from django.db import models
from Market_Product.models import Product
# Create your models here.

class HeaderBanner(models.Model):
    title = models.CharField(max_length=150,verbose_name='تیتر تخفیف')
    description = models.TextField(verbose_name='توضیحات تخفیف')
    image = models.ImageField(upload_to = 'OFF_Banners')
    go_to = models.CharField(max_length=100,verbose_name='هدایت شود به',default='/Go_to_That_Page')
    text_button = models.CharField(max_length=30,verbose_name='متن دکمه بنر تخفیف')
    active = models.BooleanField(default=False,verbose_name='نمایش داده شود')

    def __Str__(self):
        return self.title

class OFFProduct_limit_time(models.Model):
    title = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    discout_percent = models.IntegerField()
    active = models.BooleanField(default=False,verbose_name='نمایش داده شود')
    def __Str__(self):
        return self.title