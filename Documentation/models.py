from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import Q
# Create your models here

class DocManager(models.Manager):
    def search(self,query):
        lookup = (
        Q(link__title__iexact=query)
        )
        return self.get_queryset().filter(lookup).distinct()

class DocLinks(models.Model):
    title = models.TextField(verbose_name='متن لینک مساوی با لینک مستند')
    def __str__(self):
        return self.title

class Docs(models.Model):
    link = models.ForeignKey(DocLinks , on_delete=models.CASCADE)
    text = RichTextField(verbose_name='توضیحات')
    objects = DocManager()

    def __str__(self):
        return self.link.title


class ContactInfo(models.Model):
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=50)
    support = models.CharField(max_length=150)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.support

class Message(models.Model):
    name      = models.CharField(max_length=150)
    subject   = models.CharField(max_length=70)
    email     = models.CharField(max_length=170)
    message   = models.TextField()
    is_readed = models.BooleanField(default=False)

    def __str__(self):
        return self.name   