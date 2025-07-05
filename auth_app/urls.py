from django.urls import path
from .views import LoginAPIView, RegisterAPIView, ForgotPasswordAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="api_login"),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path("forgot-password/", ForgotPasswordAPIView.as_view(), name="forgot-password"),
]