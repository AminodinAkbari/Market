from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to ='profile_pic/',null = True,blank = True , default = 'default-user.png')
    gender = models.CharField(max_length=4,default='gender')

    def __str__(self):
        return str(self.user)