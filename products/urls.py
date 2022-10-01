from django.urls import path

from products import views

# ...........................users . urls
urlpatterns = [
    path('admin/addcat', views.addcat,name='addcat'),
    path('delete-cat/<int:catid>',views.deletecat, name ="delete-cat"),

]
