from django.urls import path

from insta.views import PostCreateView, SearchView

app_name = 'insta'

urlpatterns = [
    path('<int:pk>/post/create/', PostCreateView.as_view(), name='post_create'),
    path('accounts/search/', SearchView.as_view(), name='search_results'),
    # path('', PostCreateView.as_view(), name='home'),
]