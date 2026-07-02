from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from forms import SimpleSearchForm
from insta.forms import PostForm
from insta.models import Posts
# Create your views here.

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'insta/post_create.html'
    success_url = reverse_lazy('accounts:register')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        self.form = SimpleSearchForm(self.request.GET )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        return context
    