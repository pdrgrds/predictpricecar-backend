from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
import random
import string
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import status, permissions
from .serializers import UpdateProfileSerializer, ChangePasswordSerializer

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
                "phone": user.phone,
                "date_joined": user.date_joined
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

class ForgotPasswordAPIView(APIView):
    """
    Recuperar contraseña y enviar correo con la nueva
    """
    def post(self, request):
        User = get_user_model()
        email = request.data.get("email")
        if not email:
            return Response({"error": "Debe enviar el correo electrónico"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Por seguridad, no revelar que no existe
            return Response({"message": "Si el correo existe, se enviará un enlace de recuperación."})

        # Generar contraseña aleatoria
        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        user.set_password(new_password)
        user.save()

        # Enviar correo
        subject = "Recuperación de contraseña"
        html_message = render_to_string("emails/password_reset_custom.html", {
            "password": new_password,
            "nombre": user.first_name
        })
        plain_message = strip_tags(html_message)

        # Crear el correo
        msg = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=None,
            to=[email]
        )

        msg.attach_alternative(html_message, "text/html")
        msg.send()

        return Response({"message": "Si el correo existe, se enviará un enlace de recuperación."}, status=status.HTTP_200_OK)

class UpdateProfileAPIView(APIView):
    """
    Permite actualizar los datos del usuario autenticado
    """
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = request.user

        serializer = UpdateProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Datos actualizados correctamente.",
                    "data": serializer.data
                }
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

class ChangePasswordAPIView(APIView):
    """
    Permite al usuario autenticado cambiar su contraseña
    """
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        current_password = serializer.validated_data["currentPassword"]
        new_password = serializer.validated_data["newPassword"]

        if not user.check_password(current_password):
            return Response(
                {"success": False, "error": "La contraseña actual no es correcta."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()

        return Response(
            {"success": True, "message": "Contraseña actualizada correctamente."},
            status=status.HTTP_200_OK
        )
