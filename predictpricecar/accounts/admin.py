from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserType, Module

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'user_type')}),
    )

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    filter_horizontal = ('modules',)

admin.site.register(Module)