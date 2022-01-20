from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = ('fio',
                    'email',
                    )
    ordering = ('id',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',
                       'password1',
                       'password2',
                       'fio',
                       'is_proger',
                       'is_designer'
                       ), }),)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info',
         {'fields': (
             'fio',
             'is_proger',
             'is_designer'

         )}
         ),
        ('Permissions', {'fields': ('is_staff','is_superuser',)}),)

admin.site.register(User, UserAdmin)
