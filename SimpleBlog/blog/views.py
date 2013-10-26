# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from SimpleBlog.blog.models import Post
from django.contrib.auth import logout
     
def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts, 'user': request.user})
 
def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

