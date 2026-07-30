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

    @action(detail=False, methods=['get'], url_path='new')
    def new(self, request, *args, **kwargs):
        form = PostForm()

        return Response({'form': form}, template_name='insta/post_create.html')

    @action(detail=True, methods=['get'], url_path='post_up')
    def post_up(self, request, *args, **kwargs):
        post = self.get_object()
        form = PostForm(instance=post)
        context = {"post": post, "form": form}
        return Response(context, template_name='insta/post_update.html')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            form = PostForm(request.data, request.FILES)
            return Response({'form': form}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        return redirect('insta:posts-list')

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        # self.perform_update(instance)
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if not serializer.is_valid():
            if request.accepted_renderer.format == 'json':
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            form = PostForm(request.data, request.FILES, instance=instance)
            return Response({'form': form, 'post': instance}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)

        if request.accepted_renderer.format == 'json':
            return Response(serializer.data)
        return redirect('insta:posts-detail', pk=instance.pk)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        if request.accepted_renderer.format == 'json':
            return Response(status=status.HTTP_204_NO_CONTENT)
        return redirect('insta:posts-list')


    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("Вы не можете удалить чужой пост")
        instance.delete()

    # def perform_update(self, instance):
    #     if instance.author != self.request.user:
    #         raise PermissionDenied("")
    #

    @action(detail=True, methods=['get'], url_path='delete')
    def delete_confirm(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({'post': post}, template_name='insta/post_delete.html')
