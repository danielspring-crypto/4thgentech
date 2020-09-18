from django.shortcuts import render

# Create your views here.
from .models import Post 

def index(request):
	posts = Post.objects.order_by('-date')[:4]
	context = {
		'posts':posts
	}
	return render(request, 'app/index.html', context)