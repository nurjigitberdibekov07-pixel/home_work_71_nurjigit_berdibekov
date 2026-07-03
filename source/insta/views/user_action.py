from django.contrib.auth import get_user_model
from django.shortcuts import redirect, get_object_or_404


User = get_user_model()

def follow_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.user != user:
        if user in request.user.following.all():
            request.user.following.remove(user)
        else:
            request.user.following.add(user)

    return redirect('accounts:detail', user.pk)


