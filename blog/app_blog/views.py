from .models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.DRAFT)
    return render(request, 'blog/detail.html', {'post': post})
