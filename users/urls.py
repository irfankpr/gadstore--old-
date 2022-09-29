from django.urls import path, include

from users import views

# ...........................users . urls
urlpatterns = [
    path('', views.index),
    path('sign', views.sign),
    path('signin', views.signin),
    path('log', views.log),
    path('login-psw', views.login),
    path('home', views.home),
    path('products', views.products),
    path('cart', views.cart),
    path('dtl', views.dtl),
    path('chkout', views.chkout),
]
