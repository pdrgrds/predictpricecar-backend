from django.db import models
from catalogos.models import (
    MarcaVehiculo,
    ModeloVehiculo,
    VersionVehiculo,
    TipoCombustible,
    TipoTransmision,
    TipoTraccion,
    CondicionVehiculo,
    ColorVehiculo,
    TipoVehiculo
)
from django.conf import settings

class PrediccionVehiculo(models.Model):
    year_of_manufacture = models.PositiveIntegerField()
    number_of_doors = models.PositiveIntegerField()
    engine_power = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    oil_change_frequency = models.PositiveIntegerField()
    filter_change_frequency = models.PositiveIntegerField()

    engine_modifications = models.BooleanField(default=False)
    critical_replacements = models.BooleanField(default=False)
    documentation_in_order = models.BooleanField(default=False)
    taxes_in_order = models.BooleanField(default=False)
    technical_review_valid = models.BooleanField(default=False)

    # Imagenes
    front_image = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    left_side_image = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    right_side_image = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    rear_image = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    engine_image = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    interior_image = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    seats_image = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    dashboard_image = models.ImageField(upload_to='vehiculos/', null=True, blank=True)

    # Resultados de predicción
    valued_amount = models.FloatField(null=True, blank=True)
    mae = models.FloatField(null=True, blank=True)
    squared = models.FloatField(null=True, blank=True)
    rmse = models.FloatField(null=True, blank=True)

    # Relaciones con catálogos
    brand = models.ForeignKey(MarcaVehiculo, on_delete=models.CASCADE)
    model = models.ForeignKey(ModeloVehiculo, on_delete=models.CASCADE)
    version = models.ForeignKey(VersionVehiculo, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
    transmission_type = models.ForeignKey(TipoTransmision, on_delete=models.CASCADE)
    traction_type = models.ForeignKey(TipoTraccion, on_delete=models.CASCADE)
    color = models.ForeignKey(ColorVehiculo, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    
    body_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='body')
    chassis_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='chassis')
    brakes_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='brakes')
    suspension_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='suspension')
    exhaust_system_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='exhaust')
    air_conditioning_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='air_conditioning')
    electrical_system_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='electrical')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="predicciones")
    copied_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="predicciones_copiadas")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model} - {self.version} ({self.year_of_manufacture})"
