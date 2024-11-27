from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserType, Module

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('username', 'email', 'phone', 'user_type', 'password1', 'password2'),
            },
        ),
    )

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    filter_horizontal = ('modules',)

admin.site.register(Module)