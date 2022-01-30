from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from Market_Product.models import Product

class Order(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    is_paid = models.BooleanField(default=False)
    paymant_date=models.DateTimeField(blank=True,null=True)	

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount

        
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    price = models.IntegerField()
    count = models.IntegerField()
    size = models.CharField(max_length=50,default='Here Can Be Your Size')
    color = models.CharField(max_length=50,default='Here Can Be Your Selected Color')


    def get_total_price(self):
        return self.price * self.count

class UserFavorite(models.Model):
    # user = models.ForeignKey(Order,on_delete=CASCADE,blank=True,null=True)
    # favorite = models.ForeignKey(Product,on_delete=CASCADE,null=True,blank=True)
    user = models.CharField(max_length=250)
    favorite = models.ForeignKey(Product,on_delete=CASCADE,null=True,blank=True)

        