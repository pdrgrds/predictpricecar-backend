# notifications/models.py
from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Contenido en HTML")
    send_notification = models.BooleanField(default=False, help_text="Si se activa, se enviará correo al guardar")
    was_sent = models.BooleanField(default=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
