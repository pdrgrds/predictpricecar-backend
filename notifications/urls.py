from django.urls import path
from .views import CreateNotificationAPIView

urlpatterns = [
    path("create/", CreateNotificationAPIView.as_view(), name="create-notification")
]
