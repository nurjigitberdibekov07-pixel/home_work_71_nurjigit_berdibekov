from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars/', verbose_name='Avatar')
    about_me = models.TextField(max_length=500, null=True, blank=True, verbose_name='About Me')
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Phone Number')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='Gender')
    posts_count = models.PositiveIntegerField(default=0, verbose_name='Posts Count')
    followers_count = models.PositiveIntegerField(default=0, verbose_name='Followers Count')
    following_count = models.PositiveIntegerField(default=0, verbose_name='Following Count')
