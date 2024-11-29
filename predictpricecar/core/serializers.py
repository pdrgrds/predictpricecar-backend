from rest_framework import serializers
from .models import VehicleBrand, FuelType, TransmissionType, TractionType, VehicleCondition

class VehicleBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBrand
        fields = '__all__'

class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'

class TransmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionType
        fields = '__all__'

class TractionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TractionType
        fields = '__all__'

class VehicleConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCondition
        fields = '__all__'
