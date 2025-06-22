from rest_framework import serializers
from .models import PrediccionVehiculo
from catalogos.serializers import (
   MarcaVehiculoSerializer,
   ModeloVehiculoSerializer,
   VersionVehiculoSerializer,
   TipoCombustibleSerializer,
   TipoTransmisionSerializer,
   TipoTraccionSerializer,
   CondicionVehiculoSerializer,
   ColorVehiculoSerializer,
   TipoVehiculoSerializer
)

class PrediccionVehiculoSerializer(serializers.ModelSerializer):
    brand = MarcaVehiculoSerializer(read_only=True)
    model = ModeloVehiculoSerializer(read_only=True)
    version = VersionVehiculoSerializer(read_only=True)
    fuel_type = TipoCombustibleSerializer(read_only=True)
    transmission_type = TipoTransmisionSerializer(read_only=True)
    traction_type = TipoTraccionSerializer(read_only=True)
    color = ColorVehiculoSerializer(read_only=True)
    vehicle_type = TipoVehiculoSerializer(read_only=True)
    body_condition = CondicionVehiculoSerializer(read_only=True)
    chassis_condition = CondicionVehiculoSerializer(read_only=True)
    brakes_condition = CondicionVehiculoSerializer(read_only=True)
    suspension_condition = CondicionVehiculoSerializer(read_only=True)
    exhaust_system_condition = CondicionVehiculoSerializer(read_only=True)
    air_conditioning_condition = CondicionVehiculoSerializer(read_only=True)
    electrical_system_condition = CondicionVehiculoSerializer(read_only=True)

    class Meta:
        model = PrediccionVehiculo
        fields = '__all__'
        read_only_fields = ['created_at']
