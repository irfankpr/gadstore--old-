from django.contrib import admin
from products.models import Category
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class Catadmin(UserAdmin):
    ordering = ()
    list_display = ('id','category_name','slug','description','description','category_image',)
    list_display_links = ('id','category_name','slug')
    search_fields = ('id','category_name','slug')
    ordering=('id','category_name','slug')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Category,Catadmin)