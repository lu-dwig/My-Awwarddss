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

    # try:
        # posts = Post.objects.all()
        # posts = posts[::-1]
        # x = len(posts)-1
        # a_post = random.randint(1, 6)
        # random_post = posts[a_post]
        # print(random_post.photo)
    # except Post.DoesNotExist:
        # posts = None
    return render(request, 'awards/home.html',  {'form': form})

