"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import (ComparePublicationsView, FuelTypeDetailView,
                       FuelTypeListView, PublicationViewSet, RegisterView,
                       TractionTypeDetailView, TractionTypeListView,
                       TransmissionTypeDetailView, TransmissionTypeListView,
                       VehicleBrandDetailView, VehicleBrandListView,
                       VehicleConditionDetailView, VehicleConditionListView,
                       VehicleEvaluationViewSet, VehicleModelViewSet)

router = DefaultRouter()
router.register(r'evaluations', VehicleEvaluationViewSet, basename='evaluation')
router.register(r'publications', PublicationViewSet, basename='publication')
router.register(r'vehicle-models', VehicleModelViewSet, basename='vehiclemodel')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/vehicle-brands/', VehicleBrandListView.as_view(), name='vehicle-brand-list'),
    path('api/vehicle-brands/<int:pk>/', VehicleBrandDetailView.as_view(), name='vehicle-brand-detail'),
    path('api/fuel-types/', FuelTypeListView.as_view(), name='fuel-type-list'),
    path('api/fuel-types/<int:pk>/', FuelTypeDetailView.as_view(), name='fuel-type-detail'),
    path('api/transmission-types/', TransmissionTypeListView.as_view(), name='transmission-type-list'),
    path('api/transmission-types/<int:pk>/', TransmissionTypeDetailView.as_view(), name='transmission-type-detail'),
    path('api/traction-types/', TractionTypeListView.as_view(), name='traction-type-list'),
    path('api/traction-types/<int:pk>/', TractionTypeDetailView.as_view(), name='traction-type-detail'),
    path('api/vehicle-conditions/', VehicleConditionListView.as_view(), name='vehicle-condition-list'),
    path('api/vehicle-conditions/<int:pk>/', VehicleConditionDetailView.as_view(), name='vehicle-condition-detail'),
    path('api/publications/compare/', ComparePublicationsView.as_view(), name='compare-publications'),
    path('api/', include(router.urls)),
]
