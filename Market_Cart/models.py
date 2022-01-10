from django.db import models
from django.contrib.auth.models import User
from Market_Product.models import Product

class Order(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    paymant_date=models.DateTimeField(blank=True,null=True)	

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount

        
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.product.title

    def get_total_price(self):
        return self.price * self.count
        