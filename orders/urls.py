from django.urls import path, include

from users import views

# ...........................users . urls
urlpatterns = [
    path('checkout', views.checkout,name='checkout'),

]
