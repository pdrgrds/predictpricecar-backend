from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

# class UserTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserType
#         fields = '__all__'

# class CustomUserSerializer(serializers.ModelSerializer):
#     user_type = UserTypeSerializer()

#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'username', 'phone', 'user_type']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid username or password")
        self.context['user'] = user
        return data

    def get_token(self, obj):
        user = self.context['user']
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)