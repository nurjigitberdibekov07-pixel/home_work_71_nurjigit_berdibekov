from multiprocessing import context

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView
from rest_framework import viewsets

from insta.forms import PostForm, CommentsForm, SimpleSearchForm
from insta.models import Posts, Comments
from insta.serializers.posts import PostsSerializer


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Posts.objects.filter(Q(author__in=self.request.user.following.all())).order_by('-created_at')
        return Posts.objects.all()

    def list(self, request, *args, **kwargs):
        template_name = 'insta/posts_list.html'
        context = {"posts": self.get_queryset()}
        return render(request, template_name, context)

class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'insta/post_create.html'
    success_url = reverse_lazy('accounts:register')

    def has_permission(self):
        return self.request.user.pk == self.kwargs['pk']

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

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('accounts:detail', kwargs={'pk': self.request.user.pk})
        return next_url


class PostsListView(PermissionRequiredMixin, ListView):
    model = Posts
    template_name = 'insta/posts_list.html'
    context_object_name = 'posts'

    def has_permission(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_form'] = CommentsForm()
        return context

    def get_queryset(self):
        return Posts.objects.filter(Q(author__in=self.request.user.following.all())).order_by('-created_at')


class PostDetailView(PermissionRequiredMixin, DetailView):
    model = Posts
    template_name = 'insta/post_detail.html'
    context_object_name = 'post'

    def has_permission(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comments_form'] = CommentsForm()

        context['comments'] = Comments.objects.filter(post=self.object).order_by('created_at')

        return context

