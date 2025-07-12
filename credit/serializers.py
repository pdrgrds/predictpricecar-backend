from rest_framework import serializers
from .models import CreditEvaluation

class CreditEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditEvaluation
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'user']
