from django.db import models


class VehicleBrand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class FuelType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class TransmissionType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class TractionType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class VehicleCondition(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class VehicleModel(models.Model):
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.brand.name} {self.name} {self.year}"