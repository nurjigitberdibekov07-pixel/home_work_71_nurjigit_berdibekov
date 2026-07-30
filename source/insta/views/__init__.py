from insta.views.posts import PostViewSet
from insta.views.search import SearchView
from insta.views.user_action import FollowUserView, LikePostView
from insta.views.comments import comment_view, CommentDeleteView

__all__ = [
    'SearchView',
    'FollowUserView',
    'comment_view',
    'LikePostView',
    'PostViewSet',
    'CommentDeleteView'
        ]