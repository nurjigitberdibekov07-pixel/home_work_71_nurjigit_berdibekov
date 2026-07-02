from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

def get_image_path(instance, filename):
    return f'posts/{instance.author.username}/{filename}'

class Posts(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    image = models.ImageField(null=True, blank=True, upload_to=get_image_path, verbose_name='Картина')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    likes = models.ManyToManyField(get_user_model(), related_name='liked_posts', blank=True, verbose_name='Лайки')
    comments = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='Коментарии')
    created_at = models.DateTimeField(auto_now_add=True)

    def likes_count(self):
        return self.likes.count()