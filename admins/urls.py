from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from admins import views

urlpatterns = [
    path('admin/', views.index,name='admin'),
    path('admin/login', views.login),
    path('admin/logout', views.log_out,name='admin-logout'),
    path('admin/home', views.adminhome, name='adminhome'),
    path('admin/category', views.category, name='category'),
    path('admin/products', views.adm_products, name='adminproducts'),
    path('admin/addproduct', views.addproduct, name='addproduct'),
    path('admin/addnewproduct', views.add_newproduct, name='addproduct'),
    path('admin/delete-product/<int:id>/', views.deleteproduct, name='delete-product'),
    path('admin/product_dtl/<int:pid>/', views.product_dtl, name="product_dtl"),
    path('admin/users', views.users, name="users"),
    path('admin/block-users/<int:bid>/', views.block_users, name="block-user"),
]
