from django.urls import path, include

from orders import views

# ...........................users . urls
urlpatterns = [
    path('checkout', views.chkout,name='chkout'),
    path('place-order', views.place_order,name='place-order'),
    path('order-up', views.order_up, name='order-up'),

]
