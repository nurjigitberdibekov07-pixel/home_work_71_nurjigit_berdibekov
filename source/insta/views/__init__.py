from insta.views.posts import PostCreateView, PostsListView, PostDetailView
from insta.views.search import SearchView
from insta.views.user_action import follow_user
from insta.views.comments import comment_view

__all__ = [
    'PostCreateView',
    'SearchView',
    'follow_user',
    'PostsListView',
    'comment_view',
    'PostDetailView'
        ]