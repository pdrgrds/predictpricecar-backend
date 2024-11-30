from django.urls import path
from .views import VehicleEvaluationListView, VehicleEvaluationDetailView, PublicationListView

urlpatterns = [
    path('evaluations/', VehicleEvaluationListView.as_view(), name='evaluation-list'),
    path('evaluations/<int:pk>/', VehicleEvaluationDetailView.as_view(), name='evaluation-detail'),
    path('publications/', PublicationListView.as_view(), name='publication-list'),
]
