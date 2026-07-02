from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

User = get_user_model()

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user_object'

    # def get_context_data(self, **kwargs):
    #     posts = self.object.posts.all()