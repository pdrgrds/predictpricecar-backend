from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('phone',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
