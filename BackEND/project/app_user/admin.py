from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'is_active')
    search_fields = ('phone_number', 'first_name', 'last_name')
    ordering = ('phone_number',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'age', 'gender')}),
        ('Academic info', {'fields': ('course', 'major', 'student_code', 'skills')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'first_name', 'last_name'),
        }),
    )