from django.contrib import admin
from .models import VehicleEvaluation, Publication

@admin.register(VehicleEvaluation)
class VehicleEvaluationAdmin(admin.ModelAdmin):
    list_display = ('year_of_manufacture', 'model', 'valued_amount', 'user', 'evaluation_date')
    search_fields = ('model', 'user__username', 'user__email')

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'vehicle_evaluation')
    search_fields = ('title', 'user__username', 'user__email')
