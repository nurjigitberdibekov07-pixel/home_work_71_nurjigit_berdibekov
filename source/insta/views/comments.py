from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DeleteView

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



class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comments
    context_object_name = 'comment'

    def has_permission(self):
        return self.request.user.is_authenticated and self.object.author == self.request.user

    def get_success_url(self):
        return reverse('insta:posts-detail', kwargs={'pk': self.object.post.pk})



