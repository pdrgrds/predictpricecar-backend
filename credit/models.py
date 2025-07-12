from django.db import models
from django.conf import settings

class CreditEvaluation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.PositiveIntegerField(help_text="Plazo en meses")
    contact = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="credit_evaluations"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluación #{self.id} - Usuario {self.user.username}"
