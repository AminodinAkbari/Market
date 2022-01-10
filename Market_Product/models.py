from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.urls import reverse
from django.utils.timezone import now
from datetime import datetime
from Market.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.db.models import Q
from django.http import Http404

# Create your models here.

class ProductManager(models.Manager):
    def get_active_products(self):
        qs=self.get_queryset().filter(active=True)
        if qs:
            return qs
        else:
            raise Http404('Ops! Error :(')

    def get_products_by_category(self,CategoryName):
        return self.get_queryset().filter(category__url_name__iexact=CategoryName,active=True)
        
    def get_by_slug(self,slug):
        qs = Product.objects.get_queryset().filter(slug=slug)
        if qs.count()==1:
            return qs.first()
        else:
            return None

    def search(self,query):
            lookup = (
            Q(title__icontains=query) |
            Q(category__url_name__icontains=query) | 
            Q(category__title__icontains=query) |
            Q(tags__name__icontains=query)
            )
            return self.get_queryset().filter(lookup,active=True).distinct()

class Category(models.Model):
    title = models.CharField(max_length=80,verbose_name='نام')
    url_name = models.CharField(max_length=150,verbose_name='نشانی در نوار آدرس')
    image = models.ImageField(upload_to = 'Categories_images',blank=True,null = True)
    slug = models.CharField(max_length=100,default='SLUG')

    def __str__(self):
        return self.title

    def get_category_url(self):
        return f"categories/{self.url_name}"

class Tag(models.Model):
    name = models.CharField(max_length=50,verbose_name='نام برچسب')
    slug = models.SlugField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) :
        return self.name   

class Product(models.Model):
    title = models.CharField(max_length=80,verbose_name='نام')
    description = RichTextField(verbose_name='توضیحات')
    count = models.IntegerField(verbose_name='تعداد')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to = "product_images",verbose_name='تصویر')
    slug = models.SlugField(max_length=100,unique=True,blank=True,allow_unicode=True)
    tags = models.ManyToManyField(Tag,verbose_name='برچسب ها')
    off_sale = models.IntegerField(verbose_name='تخفیف(مقدار تخفیف)',default='0')
    active = models.BooleanField(default=False,verbose_name='موجود / ناموجود')

    category = models.ForeignKey(Category,on_delete = CASCADE)
    

    date = models.DateField(default=now)
    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"product_detail/{self.slug}"

    def get_product_id_for_review(self):
        return f"SendReview"/{self.id}

    def price_with_discount(self):
        return self.price - self.off_sale

    def get_by_id(self,slug):
        qs = Product.objects.get_queryset().filter(slug=slug)
        if qs.count()==1:
            return qs.first()
        else:
            return None
    def image_tag(self):
        return format_html('<img src="{}" / style="width:70px;">'.format(self.image.url))

        image_tag.short_description = 'Image'


def product_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_presave_receiver,sender=Product)


class Images(models.Model):
    name    = models.CharField(max_length=100,verbose_name='نام')
    image   = models.ImageField(verbose_name='تصویر کالا')
    product = models.ForeignKey(Product,on_delete=CASCADE)

    def __str__(self) :
        return self.name

 
class Review(models.Model):

    STATUS= (
    ('wating_for_published','در انتظار تایید'),
    ('True' , 'تایید شده'),
    ('False', 'تایید نشده')
    )
    product = models.ForeignKey(Product,on_delete = CASCADE)
    user    = models.ForeignKey(User,on_delete = CASCADE)
    rate    = models.IntegerField(default=1)
    comment = models.TextField()
    status  = models.CharField(max_length=20,choices=STATUS,default='wating_for_published')
    create_at= models.DateField(auto_now_add = True)

    def __str__(self) :
        return self.product.title

