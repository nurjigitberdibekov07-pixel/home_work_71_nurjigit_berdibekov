from django.contrib.auth.models import AbstractUser
from django.db import models

def get_avatar_path(instance, filename):
    return f'avatars/{instance.username}/{filename}'

class MyUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    avatar = models.ImageField(null=True, blank=True, upload_to=get_avatar_path, verbose_name='Аватар')
    about_me = models.TextField(max_length=500, null=True, blank=True, verbose_name='О себе')
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='Пол')
    posts_count = models.PositiveIntegerField(default=0, verbose_name='Публикации')
    followers_count = models.PositiveIntegerField(default=0, verbose_name='Подписчики')
    following_count = models.PositiveIntegerField(default=0, verbose_name='Подписки')

    def __str__(self):
        return self.username
