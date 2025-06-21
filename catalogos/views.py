from rest_framework import viewsets
from .models import (
    MarcaVehiculo,
    TipoCombustible,
    TipoTransmision,
    TipoTraccion,
    CondicionVehiculo,
    ModeloVehiculo,
    VersionVehiculo,
)
from .serializers import (
    MarcaVehiculoSerializer,
    TipoCombustibleSerializer,
    TipoTransmisionSerializer,
    TipoTraccionSerializer,
    CondicionVehiculoSerializer,
    ModeloVehiculoSerializer,
    VersionVehiculoSerializer,
)

class MarcaVehiculoViewSet(viewsets.ModelViewSet):
    queryset = MarcaVehiculo.objects.all()
    serializer_class = MarcaVehiculoSerializer

class ModeloVehiculoViewSet(viewsets.ModelViewSet):
    queryset = ModeloVehiculo.objects.all()
    serializer_class = ModeloVehiculoSerializer

class VersionVehiculoViewSet(viewsets.ModelViewSet):
    queryset = VersionVehiculo.objects.all()
    serializer_class = VersionVehiculoSerializer

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
