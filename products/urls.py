from django.urls import path
from products import views

# ...........................users . urls
urlpatterns = [
    path('admin/addcat', views.addcat, name='addcat'),
    path('delete-cat/<int:catid>', views.deletecat, name="delete-cat"),
    path('add-subcat', views.addsubcat, name="add-subcat"),
    path('addto-cart/<int:id>/', views.addto_cart, name="addto-cart"),
    path('cart-dlt/<int:id>/', views.cart_dlt, name="cart-dlt"),
    path('cart-count', views.cart_count),
]
