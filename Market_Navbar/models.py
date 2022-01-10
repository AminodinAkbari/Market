from django.db import models

# Create your models here.
class Navbar(models.Model):
    name = models.CharField(max_length=40,verbose_name='نام آیتم منو')
    url_name = models.CharField(max_length=100,verbose_name='آدرس در نوار آدرس')
    description = models.TextField(verbose_name='توضیحات این آیتم',blank=True,null=True)
    active = models.BooleanField(default=False,verbose_name='نمایش داده شود')
    class Meta:
        verbose_name = 'منوی سایت'
        verbose_name_plural = 'آیتم ها'