from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'is_staff',
        'is_active',
        'is_superuser',
        'created_at'
    ]
    list_filter = ['username', 'created_at']
    ordering = ['-created_at']


admin.site.register(User, UserAdmin)
