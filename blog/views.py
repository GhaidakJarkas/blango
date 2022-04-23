from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.utils import timezone
from blog.forms import CommentForm

# Create your views here.
def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  return render(request, 'blog/index.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_active:
      if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.content_object = post
          comment.creator = request.user
          comment.save()
          return redirect(request.path_info)
      else:
        comment_form = CommentForm()
    else:
      comment_form = None 
    return render(request, "blog/post-detail.html", {"post": post, "comment_form":comment_form})
