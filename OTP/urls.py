

from django.urls import path, include
from OTP import views

urlpatterns = [
                  path('otp', views.otp),
                  path('verify-otp', views.loginotp),

              ]
