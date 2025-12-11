from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': (
                'phone',
                'address',
                'birth_date',
                'passport_number',
                'city',
                'country',
                'gender',
                'job',
                'company',
                'extra_info',
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {
            'fields': (
                'phone',
                'address',
                'birth_date',
                'passport_number',
                'city',
                'country',
                'gender',
                'job',
                'company',
                'extra_info',
            )
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
