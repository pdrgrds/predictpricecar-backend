from django.urls import path
from .views import CreateCreditEvaluationAPIView

urlpatterns = [
    path('create/', CreateCreditEvaluationAPIView.as_view(), name="credit-create"),
]
