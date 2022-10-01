from django.db import models


# Create your models here.

class categories(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    category_image = models.ImageField(upload_to='products/category_images', blank=True)





