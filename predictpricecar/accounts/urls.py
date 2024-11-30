# from django.urls import path
# from .views import RegisterView

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
# ]

from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, ForgotPasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password')
]
