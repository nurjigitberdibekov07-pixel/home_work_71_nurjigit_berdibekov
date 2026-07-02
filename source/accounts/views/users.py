from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView

User = get_user_model()

class UserDetailView(PermissionRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user_object'

    def has_permission(self):
        return self.request.user.is_authenticated