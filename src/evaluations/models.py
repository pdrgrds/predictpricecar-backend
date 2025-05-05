from django.db import models

from accounts.models import CustomUser
from core.models import (FuelType, TractionType, TransmissionType,
                         VehicleBrand, VehicleCondition)


class VehicleEvaluation(models.Model):
    year_of_manufacture = models.PositiveIntegerField(verbose_name="Year of Manufacture")
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE, verbose_name="Brand")
    model = models.CharField(max_length=100)
    version = models.CharField(max_length=100, null=True, blank=True)
    
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, verbose_name="Fuel Type")
    color = models.CharField(max_length=50)
    transmission_type = models.ForeignKey(TransmissionType, on_delete=models.CASCADE, verbose_name="Transmission Type")
    number_of_doors = models.PositiveIntegerField()
    engine_power = models.FloatField(verbose_name="Engine Power (cc)")
    traction_type = models.ForeignKey(TractionType, on_delete=models.CASCADE, verbose_name="Traction Type")
    
    mileage = models.PositiveIntegerField(verbose_name="Historical Mileage")
    oil_change_frequency = models.CharField(max_length=100)
    filter_change_frequency = models.CharField(max_length=100)
    
    engine_modifications = models.BooleanField(default=False)
    critical_replacements = models.BooleanField(default=False)
    documentation_in_order = models.BooleanField(default=True)
    taxes_in_order = models.BooleanField(default=True)
    technical_review_valid = models.BooleanField(default=True)

    body_condition = models.ForeignKey(VehicleCondition, on_delete=models.CASCADE, related_name="body_condition")
    chassis_condition = models.ForeignKey(VehicleCondition, on_delete=models.CASCADE, related_name="chassis_condition")
    brakes_condition = models.ForeignKey(VehicleCondition, on_delete=models.CASCADE, related_name="brakes_condition")
    suspension_condition = models.ForeignKey(VehicleCondition, on_delete=models.CASCADE, related_name="suspension_condition")
    exhaust_system_condition = models.ForeignKey(VehicleCondition, on_delete=models.CASCADE, related_name="exhaust_system_condition")
    air_conditioning_condition = models.ForeignKey(VehicleCondition, on_delete=models.CASCADE, related_name="air_conditioning_condition")
    electrical_system_condition = models.ForeignKey(VehicleCondition, on_delete=models.CASCADE, related_name="electrical_system_condition")
    
    front_image = models.ImageField(upload_to="evaluations/images/", null=True, blank=True)
    left_side_image = models.ImageField(upload_to="evaluations/images/", null=True, blank=True)
    right_side_image = models.ImageField(upload_to="evaluations/images/", null=True, blank=True)
    rear_image = models.ImageField(upload_to="evaluations/images/", null=True, blank=True)
    engine_image = models.ImageField(upload_to="evaluations/images/", null=True, blank=True)
    interior_image = models.ImageField(upload_to="evaluations/images/", null=True, blank=True)
    seats_image = models.ImageField(upload_to="evaluations/images/", null=True, blank=True)
    dashboard_image = models.ImageField(upload_to="evaluations/images/", null=True, blank=True)
    
    valued_amount = models.DecimalField(max_digits=10, decimal_places=2)
    mae = models.FloatField()
    squared = models.FloatField()
    rmse = models.FloatField()
    evaluation_date = models.DateField(auto_now_add=True)
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="evaluations")
    copied_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name="copied_evaluations", null=True, blank=True)
    
    def __str__(self):
        return f"{self.year_of_manufacture} {self.model} ({self.user.username})"

class Publication(models.Model):
    vehicle_evaluation = models.ForeignKey(VehicleEvaluation, on_delete=models.CASCADE, verbose_name="Vehicle Evaluation")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="User")
    status = models.CharField(max_length=50, choices=[
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("sold", "Sold")
    ])
    title = models.CharField(max_length=100)
    description = models.TextField()
    main_image = models.ImageField(upload_to="publications/images/", null=True, blank=True)
    
    def __str__(self):
        return self.title
