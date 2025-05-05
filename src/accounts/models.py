from django.contrib.auth.models import AbstractUser
from django.db import models


class Module(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    modules = models.ManyToManyField(Module, related_name="user_types", blank=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.ForeignKey('UserType', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username