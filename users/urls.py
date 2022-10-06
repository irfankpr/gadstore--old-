from django.urls import path, include

from users import views

# ...........................users . urls
urlpatterns = [
    path('', views.index),
    path('sign', views.sign),
    path('signin', views.signin),
    path('log', views.log,name="log"),
    path('logotp', views.loginotp),
    path('login-psw', views.login),
    path('home', views.home),
    path('products', views.shop),
    path('cartv', views.cartv,name='cartv'),
    path('detail/<int:id>', views.dtl,name='detail'),
    path('chkout', views.chkout),
    path('login-otp', views.loginotp),
    path('usr-logout', views.usr_logout),
    path('landing', views.landing,name='landing'),
]
