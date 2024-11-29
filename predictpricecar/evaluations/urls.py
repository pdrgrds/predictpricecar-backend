from django.urls import path
from .views import VehicleEvaluationListView, PublicationListView

urlpatterns = [
    path('evaluations/', VehicleEvaluationListView.as_view(), name='evaluation-list'),
    path('publications/', PublicationListView.as_view(), name='publication-list'),
]
