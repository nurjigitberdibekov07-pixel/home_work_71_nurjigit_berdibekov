from django.contrib.auth import get_user_model
from django.db import models


class Comments(models.Model):
    post = models.ForeignKey('insta.Posts', on_delete=models.CASCADE, related_name='Comments', verbose_name='Пост')
    text = models.TextField(max_length=400, verbose_name='Комментарий', null=True, blank=True)
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    # def get_absolute_url(self):
    #     pass
