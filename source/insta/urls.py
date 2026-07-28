
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from insta.views import (PostCreateView, SearchView, FollowUserView, PostsListView, comment_view, PostDetailView,
                         LikePostView, PostViewSet)

app_name = 'insta'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/post/create/', PostCreateView.as_view(), name='post_create'),
    path('accounts/search/', SearchView.as_view(), name='search_results'),
    path('<int:pk>/followers/', FollowUserView.as_view(), name='follow_user'),
    path('posts/', PostsListView.as_view(), name='posts_list'),
    path('post/<int:pk>/comment/', comment_view, name='comment'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/like', LikePostView.as_view(), name='like'),
    path('login/', obtain_auth_token, name='api_token_auth')
]