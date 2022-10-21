from django.db import models
from django.db.models import Model
from products.models import products,categories
from profiles.models import userprofiles, address


# Create your models here.


class Coupons(models.Model):
    Coupon_code = models.CharField(max_length=100)
    minimum = models.FloatField(default=False)
    discount_rate = models.FloatField()
    discount_type = models.CharField(max_length=50, default='FLAT', choices=(('FLAT', 'FLAT'), ('UPTO', 'UPTO')))




class orders(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    user = models.ForeignKey(userprofiles, on_delete=models.CASCADE)
    address = models.ForeignKey(address, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    Total = models.FloatField()
    payment = models.CharField(max_length=100, default='COD')
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')
    payment_id = models.CharField(max_length=500, null=True)
    Offer_applied = models.CharField(max_length=100, default=False)
    Coupon_applied = models.ForeignKey(Coupons, on_delete=models.CASCADE,null=True,default=False)
    discount_rate = models.FloatField(default=0)









