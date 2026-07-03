from django.urls import path

from insta.views import PostCreateView, SearchView, follow_user, PostsListView, comment_view, PostDetailView

app_name = 'insta'

urlpatterns = [
    path('<int:pk>/post/create/', PostCreateView.as_view(), name='post_create'),
    path('accounts/search/', SearchView.as_view(), name='search_results'),
    path('<int:pk>/followers/', follow_user, name='follow_user'),
    path('posts/', PostsListView.as_view(), name='posts_list'),
    path('post/<int:pk>/comment/', comment_view, name='comment'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='detail'),
]