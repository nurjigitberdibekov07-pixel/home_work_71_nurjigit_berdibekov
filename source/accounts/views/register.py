from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

from accounts.forms import MyUserCreationForm
from accounts.models import Profile

User = get_user_model()

class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(
            user=user,
            avatar=form.cleaned_data.get('avatar'),
            about_me=form.cleaned_data.get('about_me'),
            phone_number=form.cleaned_data.get('phone_number'),
            gender=form.cleaned_data.get('gender'),
        )
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('accounts:register')
        return next_url