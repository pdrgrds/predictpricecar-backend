from django.urls import path
from .views import (
    VehicleBrandListView, VehicleBrandDetailView,
    FuelTypeListView, FuelTypeDetailView,
    TransmissionTypeListView, TransmissionTypeDetailView,
    TractionTypeListView, TractionTypeDetailView,
    VehicleConditionListView, VehicleConditionDetailView
)

urlpatterns = [
    path('vehicle-brands/', VehicleBrandListView.as_view(), name='vehicle-brand-list'),
    path('vehicle-brands/<int:pk>/', VehicleBrandDetailView.as_view(), name='vehicle-brand-detail'),
    path('fuel-types/', FuelTypeListView.as_view(), name='fuel-type-list'),
    path('fuel-types/<int:pk>/', FuelTypeDetailView.as_view(), name='fuel-type-detail'),
    path('transmission-types/', TransmissionTypeListView.as_view(), name='transmission-type-list'),
    path('transmission-types/<int:pk>/', TransmissionTypeDetailView.as_view(), name='transmission-type-detail'),
    path('traction-types/', TractionTypeListView.as_view(), name='traction-type-list'),
    path('traction-types/<int:pk>/', TractionTypeDetailView.as_view(), name='traction-type-detail'),
    path('vehicle-conditions/', VehicleConditionListView.as_view(), name='vehicle-condition-list'),
    path('vehicle-conditions/<int:pk>/', VehicleConditionDetailView.as_view(), name='vehicle-condition-detail'),
]
