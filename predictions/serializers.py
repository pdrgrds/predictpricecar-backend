from rest_framework import serializers
from .models import PrediccionVehiculo

class PrediccionVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrediccionVehiculo
        fields = '__all__'
        read_only_fields = ['valued_amount', 'mae', 'squared', 'rmse', 'created_at']
