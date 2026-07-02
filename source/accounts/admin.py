from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import MyUser

class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {
            'fields': ('avatar', 'about_me', 'phone_number', 'gender', 'posts_count', 'followers_count', 'following_count')
        }),
    )


admin.site.register(MyUser, MyUserAdmin)