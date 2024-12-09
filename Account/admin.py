from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )
    list_display = ('email', 'username', 'role', 'is_active', 'is_staff')

admin.site.register(User, CustomUserAdmin)