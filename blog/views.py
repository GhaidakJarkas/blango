from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.
def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  return render(request, 'blog/index.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post-detail.html", {"post": post})
