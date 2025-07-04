from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

class LoginAPIView(APIView):
    """
    API de login que devuelve un token JWT y los datos del usuario
    """
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Por favor, ingrese usuario y contraseña."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Usuario/Contraseña incorrectas"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_active:
            return Response(
                {"error": "Usuario dado de baja. Contacte al administrador."},
                status=status.HTTP_403_FORBIDDEN
            )

        refresh = RefreshToken.for_user(user)
        return Response({
            "token": str(refresh.access_token),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "is_staff": user.is_staff,
            }
        })

class RegisterAPIView(APIView):
    """
    API de registro de usuario
    """
    def post(self, request):
        User = get_user_model()
        data = request.data

        required_fields = ['username', 'email', 'password', 'phone', 'first_name', 'last_name']
        for field in required_fields:
            if not data.get(field):
                return Response(
                    {"success": False, "error": f"El campo '{field}' es obligatorio."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        if User.objects.filter(username=data['username']).exists():
            return Response(
                {"success": False, "error": "El nombre de usuario ya existe."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if User.objects.filter(email=data['email']).exists():
            return Response(
                {"success": False, "error": "El correo electrónico ya está registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Crear usuario
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            phone=data['phone'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            is_active=True,
        )

        return Response(
            {"success": True},
            status=status.HTTP_201_CREATED
        )
