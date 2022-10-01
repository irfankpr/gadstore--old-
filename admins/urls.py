from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from admins import views


urlpatterns = [
    path('',views.log),
    path('login',views.login),
    path('adminhome',views.adminhome, name='adminhome'),
    path('category',views.category, name='category')
]