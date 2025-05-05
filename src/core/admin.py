from django.contrib import admin

from .models import (FuelType, TractionType, TransmissionType, VehicleBrand,
                     VehicleCondition, VehicleModel)

admin.site.register(VehicleBrand)
admin.site.register(FuelType)
admin.site.register(TransmissionType)
admin.site.register(TractionType)
admin.site.register(VehicleCondition)

@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'year']
    search_fields = ['name']
    list_filter = ['brand', 'year']