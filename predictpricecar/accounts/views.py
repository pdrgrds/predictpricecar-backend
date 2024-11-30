# from django.contrib.auth.views import LoginView
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
# from .forms import CustomUserCreationForm

# class RegisterView(CreateView):
#     template_name = 'registration/register.html'
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')

# class CustomLoginView(LoginView):
#     template_name = 'registration/login.html'

from decouple import config
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core.mail import send_mail
from .utils import generate_random_password
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.context['user']
        return Response({
            "token": serializer.data.get('token'),
            "user": UserSerializer(user).data
        }, status=status.HTTP_200_OK)

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'El correo es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'message': 'Se envio una nueva contraseña a tu correo.'}, status=status.HTTP_200_OK)

        new_password = generate_random_password()
        user.set_password(new_password)
        user.save()

        send_mail(
            'Nueva contraseña',
            f'Hola {user.username},\n\nTu nueva contraseña es: {new_password}\n\nPor favor, cambiala luego de iniciar sesión.',
            config('EMAIL_HOST_USER'),
            [user.email],
            fail_silently=False,
        )

        return Response({'message': 'Se envio una nueva contraseña a tu correo.'}, status=status.HTTP_200_OK)

