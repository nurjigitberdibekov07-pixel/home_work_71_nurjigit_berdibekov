from rest_framework import serializers
from django.contrib.auth import get_user_model

from insta.models.post import Posts


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


class PostsSerializer(serializers.ModelSerializer):
    likes = UserShortSerializer(many=True, read_only=True)
    likes_to_save = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        source='likes',
        queryset=get_user_model().objects.all(),
    )

    class Meta:
        model = Posts
        fields = ['id', 'author', 'image', 'likes', 'likes_to_save', 'description', 'created_at']
        read_only_fields = ['id', 'author', 'likes', 'created_at']