from rest_framework import viewsets
from .models import (
    MarcaVehiculo,
    TipoCombustible,
    TipoTransmision,
    TipoTraccion,
    CondicionVehiculo
)
from .serializers import (
    MarcaVehiculoSerializer,
    TipoCombustibleSerializer,
    TipoTransmisionSerializer,
    TipoTraccionSerializer,
    CondicionVehiculoSerializer
)

class MarcaVehiculoViewSet(viewsets.ModelViewSet):
    queryset = MarcaVehiculo.objects.all()
    serializer_class = MarcaVehiculoSerializer

class TipoCombustibleViewSet(viewsets.ModelViewSet):
    queryset = TipoCombustible.objects.all()
    serializer_class = TipoCombustibleSerializer

class TipoTransmisionViewSet(viewsets.ModelViewSet):
    queryset = TipoTransmision.objects.all()
    serializer_class = TipoTransmisionSerializer

class TipoTraccionViewSet(viewsets.ModelViewSet):
    queryset = TipoTraccion.objects.all()
    serializer_class = TipoTraccionSerializer

class CondicionVehiculoViewSet(viewsets.ModelViewSet):
    queryset = CondicionVehiculo.objects.all()
    serializer_class = CondicionVehiculoSerializer
