from rest_framework import serializers
from .models import (
    MarcaVehiculo,
    TipoCombustible,
    TipoTransmision,
    TipoTraccion,
    CondicionVehiculo
)

class MarcaVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaVehiculo
        fields = '__all__'

class TipoCombustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCombustible
        fields = '__all__'

class TipoTransmisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTransmision
        fields = '__all__'

class TipoTraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTraccion
        fields = '__all__'

class CondicionVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicionVehiculo
        fields = '__all__'
