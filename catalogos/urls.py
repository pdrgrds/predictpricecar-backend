from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'marcas', views.MarcaVehiculoViewSet)
router.register(r'modelo', views.ModeloVehiculoViewSet)
router.register(r'version', views.VersionVehiculoViewSet)
router.register(r'combustibles', views.TipoCombustibleViewSet)
router.register(r'transmisiones', views.TipoTransmisionViewSet)
router.register(r'tracciones', views.TipoTraccionViewSet)
router.register(r'condiciones', views.CondicionVehiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
