
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from insta.views import (SearchView, FollowUserView,  comment_view,
                         LikePostView, PostViewSet, CommentDeleteView)

app_name = 'insta'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/search/', SearchView.as_view(), name='search_results'),
    path('<int:pk>/followers/', FollowUserView.as_view(), name='follow_user'),
    path('post/<int:pk>/comment/', comment_view, name='comment'),
    path('post/<int:pk>/like', LikePostView.as_view(), name='like'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]