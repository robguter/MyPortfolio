from django.shortcuts import render, get_object_or_404
from .models import Post

def rndr_psts(request):
    posts = Post.objects.all()
    return render(request, 'blog.htm', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.htm', {'post': post})