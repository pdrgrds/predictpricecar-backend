from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from auth_app.models import CustomUser
from .serializers import NotificationSerializer

class CreateNotificationAPIView(APIView):
    """
    Crear una notificación y enviar correo si está habilitado.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            notification = serializer.save()

            if notification.send_notification:
                users = CustomUser.objects.filter(permitir_notifications=True, is_active=True)
                for user in users:
                    html_message = notification.content
                    plain_message = strip_tags(html_message)
                    send_mail(
                        subject=notification.title,
                        message=plain_message,
                        html_message=html_message,
                        from_email=None,
                        recipient_list=[user.email],
                        fail_silently=False
                    )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
