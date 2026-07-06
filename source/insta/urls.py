from django.urls import path

from insta.views import (PostCreateView, SearchView, FollowUserView, PostsListView, comment_view, PostDetailView,
                         LikePostView)

app_name = 'insta'

urlpatterns = [
    path('<int:pk>/post/create/', PostCreateView.as_view(), name='post_create'),
    path('accounts/search/', SearchView.as_view(), name='search_results'),
    path('<int:pk>/followers/', FollowUserView.as_view(), name='follow_user'),
    path('posts/', PostsListView.as_view(), name='posts_list'),
    path('post/<int:pk>/comment/', comment_view, name='comment'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/like', LikePostView.as_view(), name='like'),
]