from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone_number', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('phone_number', 'email', 'first_name', 'last_name', 'is_verified', 'is_staff', 'is_superuser')

class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User

    list_display = ('phone_number', 'email', 'is_verified', 'is_staff', 'is_superuser')
    readonly_fields = ('created_at',)
    ordering = ('phone_number',)  # username биш phone_number

    fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'age', 'gender', 'course', 'major', 'student_code', 'skills')}),
        ('Permissions', {'fields': ('is_verified','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(User, UserAdmin)