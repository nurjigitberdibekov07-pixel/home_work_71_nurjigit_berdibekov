from django.urls import path
from insta.views import PostCreateView

urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name='post_create'),
]