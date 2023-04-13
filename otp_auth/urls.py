from django.urls import path
from .views import *
from task_app.views import *

urlpatterns = [
    path('login_otp_send',LoginNumberOtpAPIView.as_view()),
    path('signup_otp_send',RegNumberOtpAPIView.as_view()),
    path('user_create',CreateAPIView.as_view()),
    path('signin/',login),
    path('signup/',signup),
]
