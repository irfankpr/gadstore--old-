from django.db import models
from django.db.models import Model
from products.models import products
from profiles.models import userprofiles, address


# Create your models here.


class orders(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    user = models.ForeignKey(userprofiles, on_delete=models.CASCADE)
    address = models.ForeignKey(address, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    Total = models.FloatField()
    payment = models.CharField(max_length=100, default='COD')
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')
