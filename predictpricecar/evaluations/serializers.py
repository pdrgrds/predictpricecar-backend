from rest_framework import serializers
from .models import VehicleEvaluation, Publication

class VehicleEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleEvaluation
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'