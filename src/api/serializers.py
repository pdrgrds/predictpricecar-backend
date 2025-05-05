# src/apis/serializers.py

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from core.models import (FuelType, TractionType, TransmissionType,
                         VehicleBrand, VehicleCondition, VehicleModel)
from evaluations.models import Publication, VehicleEvaluation

# from accounts.models import CustomUser

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'user_type']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            user_type=validated_data['user_type']
        )
        return user
    
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

class VehicleEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleEvaluation
        fields = '__all__'
        read_only_fields = ['evaluation_date', 'user', 'copied_user']

class PublicationSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='vehicle_evaluation.brand.name', read_only=True)
    model = serializers.CharField(source='vehicle_evaluation.model', read_only=True)
    year = serializers.IntegerField(source='vehicle_evaluation.year_of_manufacture', read_only=True)
    estimated_price = serializers.DecimalField(
        source='vehicle_evaluation.valued_amount', max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Publication
        fields = [
            'id', 
            'vehicle_evaluation',
            'title', 
            'description', 
            'main_image', 
            'status', 
            'brand', 
            'model', 
            'year', 
            'estimated_price'
        ]
        read_only_fields = ['brand', 'model', 'year', 'estimated_price']

class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'