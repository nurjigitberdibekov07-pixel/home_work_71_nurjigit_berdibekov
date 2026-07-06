from django.shortcuts import redirect, get_object_or_404

from insta.forms import CommentsForm
from insta.models import Posts, Comments


def comment_view(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            post = get_object_or_404(Posts, pk=pk)
            form = CommentsForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()

    redirect_url = 'insta:posts_list'
    if request.GET.get('next'):
            redirect_url = request.GET.get('next')
    if request.POST.get('next'):
            redirect_url = request.POST.get('next')
    return redirect(redirect_url)







