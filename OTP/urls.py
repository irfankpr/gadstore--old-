from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from OTP import views

urlpatterns = [
                  path('otp', views.otp),
                  path('verify-otp', views.loginotp),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
