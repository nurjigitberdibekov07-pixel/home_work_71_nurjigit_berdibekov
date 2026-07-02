from django.contrib import admin
from insta.models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'image', 'description', 'comments', 'created_at']
    list_filter = ['author', 'created_at']
    search_fields = ['id']
    fields = ['author', 'image', 'description', 'comments', 'likes', 'created_at']
    readonly_fields = ['created_at']
    filter_horizontal = ['likes']

admin.site.register(Posts, PostsAdmin)