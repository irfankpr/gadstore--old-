from django.db import models

# Create your models here.
class Category(models.Model):
    category_name= models.BooleanField(max_length=50,unique=True)
    slug = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True)
    category_image = models.ImageField(upload_to='products/category_images',blank=True)

    def __str__(self):
        return self.category_name
