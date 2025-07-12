# notifications/admin.py
from django.contrib import admin
from .models import Notification
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.html import strip_tags
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.html import strip_tags

User = get_user_model()

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'send_notification', 'was_sent', 'created_at')
    readonly_fields = ('created_at', 'was_sent')

    def save_model(self, request, obj, form, change):
        send_email = False

        if not change:
            # Creación
            if obj.send_notification:
                send_email = True
        else:
            # Edición
            old_obj = Notification.objects.get(pk=obj.pk)
            if not old_obj.was_sent and obj.send_notification:
                send_email = True

        # Guardar primero
        super().save_model(request, obj, form, change)

        if send_email:
            recipients = User.objects.filter(permitir_notifications=True).values_list('email', flat=True)
            if recipients:
                subject = obj.title

                html_content = render_to_string("emails/notification_email.html", {
                    "title": obj.title,
                    "content": obj.content,  # Aquí va el HTML que el admin haya puesto
                })

                # También se genera una versión de texto plano
                text_content = strip_tags(html_content)

                # Preparar y enviar correo
                email = EmailMultiAlternatives(
                    subject=obj.title,
                    body=text_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[],
                    bcc=list(recipients)
                )
                email.attach_alternative(html_content, "text/html")
                email.send()

                obj.was_sent = True
                obj.save()

                messages.success(request, f"✅ Notificación enviada a {len(recipients)} usuarios.")
            else:
                messages.warning(request, "⚠️ No hay usuarios con notificaciones habilitadas.")
