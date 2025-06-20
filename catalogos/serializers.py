from rest_framework import serializers
from .models import (
    MarcaVehiculo,
    ModeloVehiculo,
    VersionVehiculo,
    TipoCombustible,
    TipoTransmision,
    TipoTraccion,
    CondicionVehiculo
)

class MarcaVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaVehiculo
        fields = '__all__'

class ModeloVehiculoSerializer(serializers.ModelSerializer):
    marca = MarcaVehiculoSerializer()

    class Meta:
        model = ModeloVehiculo
        fields = '__all__'

class VersionVehiculoSerializer(serializers.ModelSerializer):
    modelo = ModeloVehiculoSerializer()

    class Meta:
        model = VersionVehiculo
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
