from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.contrib.auth import get_user_model

from accounts.forms import MyUserCreationForm
from forms import SimpleSearchForm

User = get_user_model()

class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def dispatch(self, request, *args, **kwargs):
        self.form = SimpleSearchForm(self.request.GET )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('accounts:register')
        return next_url