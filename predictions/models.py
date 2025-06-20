from django.db import models
from catalogos.models import (
    MarcaVehiculo,
    TipoCombustible,
    TipoTransmision,
    TipoTraccion,
    CondicionVehiculo
)
from django.contrib.auth.models import User

class PrediccionVehiculo(models.Model):
    year_of_manufacture = models.PositiveIntegerField()
    model = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
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
    fuel_type = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
    transmission_type = models.ForeignKey(TipoTransmision, on_delete=models.CASCADE)
    traction_type = models.ForeignKey(TipoTraccion, on_delete=models.CASCADE)
    
    body_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='body')
    chassis_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='chassis')
    brakes_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='brakes')
    suspension_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='suspension')
    exhaust_system_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='exhaust')
    air_conditioning_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='air_conditioning')
    electrical_system_condition = models.ForeignKey(CondicionVehiculo, on_delete=models.SET_NULL, null=True, related_name='electrical')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    copied_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='copied_predictions')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model} - {self.version} ({self.year_of_manufacture})"
