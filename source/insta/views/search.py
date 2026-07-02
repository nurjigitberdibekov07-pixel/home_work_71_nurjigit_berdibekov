from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import ListView

from forms import SimpleSearchForm

User = get_user_model()

class SearchView(LoginRequiredMixin, ListView):
    template_name = 'insta/users_list.html'
    model = User
    context_object_name = 'users'

    def dispatch(self, request, *args, **kwargs):
        self.form = SimpleSearchForm(self.request.GET )
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_value:
            queryset = queryset.filter(Q(username__icontains=self.search_value) | Q(email__icontains=self.search_value) | Q(first_name__icontains=self.search_value))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context