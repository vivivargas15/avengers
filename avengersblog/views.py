from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def home(request):
	return render(request, 'avengersblog/home.html')

def blog(request):
	posts=Post.objects.all()
	return render(request, 'avengersblog/blog.html', {'posts':posts})


def blog_detail(request,pk):
	posts=get_object_or_404(Post, pk=pk)
	return render(request, 'avengersblog/blog_detail.html', {'posts':posts})