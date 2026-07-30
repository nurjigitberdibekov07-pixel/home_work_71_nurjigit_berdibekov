from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from insta.models.post import Posts


User = get_user_model()

class FollowUserView(LoginRequiredMixin, View):
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)

        if request.user != user:
            if user in request.user.following.all():
                request.user.following.remove(user)
            else:
                request.user.following.add(user)

        next_url = request.POST.get('next') or request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('accounts:detail', pk=user.pk)


class LikePostView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Posts, pk=kwargs['pk'])

        if request.user not in post.likes.all():
            post.likes.add(request.user)
            liked = True
        else:
            post.likes.remove(request.user)
            liked = False

        return JsonResponse({"like": liked, "count": post.likes_count()})
