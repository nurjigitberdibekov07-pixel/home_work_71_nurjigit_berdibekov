from django.db.models import Q
from django.shortcuts import redirect

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from insta.forms import PostForm, CommentsForm
from insta.models import Posts, Comments
from insta.serializers.posts import PostsSerializer


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'insta/post_detail.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Posts.objects.filter(Q(author__in=self.request.user.following.all()) | Q(author=self.request.user)).order_by('-created_at')
        return Posts.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_template_names(self):
        if self.action == 'list':
            return ['insta/posts_list.html']
        elif self.action == 'retrieve':
            return ['insta/post_detail.html']
        elif self.action == 'create':
            return ['insta/post_create.html']
        elif self.action in ['update', 'partial_update']:
            return ['insta/post_update.html']
        elif self.action == 'destroy':
            return ['insta/post_delete.html']

    def list(self, request, *args, **kwargs):
        posts = self.get_queryset()
        context = {"posts": posts, "comments_form": CommentsForm()}
        return Response(context)

    def retrieve(self, request, *args, **kwargs):
        post = self.get_queryset().get(pk=self.kwargs['pk'])
        serializer = self.get_serializer(post)

        if request.accepted_renderer.format == 'json':
            return Response(serializer.data)

        context = {
            "post": post,
            "serializer": serializer,
            "comments_form": CommentsForm(),
            "comments": Comments.objects.filter(post=post).order_by('-created_at')
        }
        return Response(context, status=status.HTTP_200_OK)

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

