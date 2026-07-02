from django.urls import path

from insta.views import PostCreateView

app_name = 'insta'

urlpatterns = [
    path('<int:pk>/post/create/', PostCreateView.as_view(), name='post_create'),
]