from django.contrib import admin
from insta.models import Posts, Comments

class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'image', 'description', 'comments', 'created_at']
    list_filter = ['author', 'created_at']
    search_fields = ['id']
    fields = ['author', 'image', 'description', 'comments', 'likes', 'created_at']
    readonly_fields = ['created_at']
    filter_horizontal = ['likes']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'post', 'text']
    list_filter = ['author', 'created_at']
    search_fields = ['id']
    fields = ['author', 'text']
    readonly_fields = ['created_at']


admin.site.register(Comments, CommentsAdmin)
admin.site.register(Posts, PostsAdmin)