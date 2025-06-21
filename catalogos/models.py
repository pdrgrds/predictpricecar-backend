from django.db import models


class MarcaVehiculo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Marca")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    company = models.CharField(max_length=100, verbose_name="Compañía")

    def __str__(self):
        return self.name

class ModeloVehiculo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Modelo")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    marca = models.ForeignKey(MarcaVehiculo, on_delete=models.CASCADE, related_name="modelos", verbose_name="Marca")

    def __str__(self):
        return f"{self.marca.name} {self.name}"

class VersionVehiculo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Versión")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    modelo = models.ForeignKey(ModeloVehiculo, on_delete=models.CASCADE, related_name="versiones", verbose_name="Modelo")

    def __str__(self):
        return f"{self.modelo.name} {self.name}"

class TipoCombustible(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class TipoTransmision(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class TipoTraccion(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class CondicionVehiculo(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
