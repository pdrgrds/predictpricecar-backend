from django.contrib import admin
from .models import PrediccionVehiculo

@admin.register(PrediccionVehiculo)
class PrediccionVehiculoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'model',
        'version',
        'year_of_manufacture',
        'brand',
        'fuel_type',
        'valued_amount',
        'user',
        'created_at',
    )
    list_filter = ('brand', 'fuel_type', 'transmission_type', 'traction_type', 'created_at')
    search_fields = ('model', 'version', 'user__username')
    readonly_fields = ('valued_amount', 'mae', 'rmse', 'squared', 'created_at')
