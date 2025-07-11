from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrediccionVehiculoViewSet, UserPredictionsListAPIView, predecir_y_guardar, ListPrediccionesFilteredAPIView, PredictionFiltersAPIView

router = DefaultRouter()
router.register(r'historial', PrediccionVehiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('predecir/', predecir_y_guardar, name='predecir_y_guardar'),
    path("my-predictions/", UserPredictionsListAPIView.as_view(), name="user-predictions"),
    path("list-filtered/", ListPrediccionesFilteredAPIView.as_view(), name="list-predicciones-filtered"),
    path("filters/", PredictionFiltersAPIView.as_view(), name="prediction-filters"),
]