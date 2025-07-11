from rest_framework import serializers
from .models import CustomUser

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'permitir_notifications']

class ChangePasswordSerializer(serializers.Serializer):
    currentPassword = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=True)
    confirmNewPassword = serializers.CharField(required=True)

    def validate(self, data):
        if data["newPassword"] != data["confirmNewPassword"]:
            raise serializers.ValidationError("La nueva contraseña y la confirmación no coinciden.")
        return data

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "is_active",
            "is_staff",
            "date_joined"
        ]
