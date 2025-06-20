from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrediccionVehiculoViewSet, predecir_y_guardar

router = DefaultRouter()
router.register(r'historial', PrediccionVehiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('predecir/', predecir_y_guardar, name='predecir_y_guardar')
]