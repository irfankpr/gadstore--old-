from django.contrib import admin
from products.models import categories
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(categories)