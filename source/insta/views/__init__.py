from insta.views.posts import PostCreateView, PostsListView, PostDetailView, PostViewSet
from insta.views.search import SearchView
from insta.views.user_action import FollowUserView, LikePostView
from insta.views.comments import comment_view

__all__ = [
    'PostCreateView',
    'SearchView',
    'FollowUserView',
    'PostsListView',
    'comment_view',
    'PostDetailView',
    'LikePostView',
    'PostViewSet'
        ]