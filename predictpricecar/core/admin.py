from django.contrib import admin
from .models import (
    VehicleBrand,
    FuelType,
    TransmissionType,
    TractionType,
    VehicleCondition
)

admin.site.register(VehicleBrand)
admin.site.register(FuelType)
admin.site.register(TransmissionType)
admin.site.register(TractionType)
admin.site.register(VehicleCondition)