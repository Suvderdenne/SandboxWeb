from django.urls import path
from .views import signup_view, signin_view, verify_otp

urlpatterns = [
    path('signup/', signup_view),
    path('signin/', signin_view),
    path('verify-otp/', verify_otp),
]