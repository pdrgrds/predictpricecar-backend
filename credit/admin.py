from django.contrib import admin
from .models import CreditEvaluation

@admin.register(CreditEvaluation)
class CreditEvaluationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'term', 'contact', 'created_at')
    list_filter = ('contact', 'created_at')
    search_fields = ('user__username',)
