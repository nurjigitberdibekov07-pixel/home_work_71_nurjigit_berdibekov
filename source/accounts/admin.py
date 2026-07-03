from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import MyUser

class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {
            'fields': ('avatar', 'about_me', 'phone_number', 'gender', 'following')
        }),
    )


admin.site.register(MyUser, MyUserAdmin)