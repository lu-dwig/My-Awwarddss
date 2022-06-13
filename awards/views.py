from django.shortcuts import render
from .models import Post
from users.forms import  PostForm, RatingsForm
from pyuploadcare.dj.forms import ImageField
import random

# Create your views here.
def home(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        post = posts
        posts = Post.objects.all()
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    return render(request, 'awards/home.html',  {'form': form})

def searchPhoto(request):
    query = request.GET.get('query')
    if query != None:
        post= Post.objects.filter(title__contains='spice')

    context = {
        'posts': post,
        'title':'search post'
    }
    return render(request, 'awards/search.html', context)
 
