from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
	return render(request, 'avengersblog/home.html')

def blog(request):
	posts=Post.objects.all()
	return render(request, 'avengersblog/blog.html', {'posts':posts})