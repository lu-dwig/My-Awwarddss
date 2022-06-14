from django.shortcuts import render, redirect
from .models import Post, Ratings
from users.forms import  PostForm, RatingsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from pyuploadcare.dj.forms import ImageField
import requests

# Create your views here.
def home(request):
    response = ''
    url = 'http://127.0.0.1:8000/api/postList/'
    res = requests.get(url)
    if (res.status_code == 200):
        response = res.json()
        print(response)
        
    context = {
        'posts': response,
    }
        
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     post = posts
    #     posts = Post.objects.all()
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user
    #         post.save()
    # else:
    #     form = PostForm()

    return render(request, 'awards/home.html',  context)

def searchPhoto(request):
    query = request.GET.get('query')
    if query != None:
        post= Post.objects.filter(title__contains='spice')

    context = {
        'posts': post,
        'title':'search post'
    }
    return render(request, 'awards/search.html', context)

@login_required(login_url='login') 
def detail(request,pk):
    url = f'http://127.0.0.1:8000/postDetail/{pk}/'
    res = requests.get(url)
    if (res.status_code == 200):
        response = res.json()
        print(response)
    post = Post.objects.get(id=pk)
    ratings = Ratings.objects.filter(post=post)
    form = RatingsForm()

    rated = False

    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            ratings = form.save(commit=True)
            ratings.user = request.user
            ratings.project = post
            ratings.save()
            messages.success(request, f'You have successfully voted!')
            rated = True
            return redirect('detail')
        else:
            messages.success(request, f'Failed!')
    else:
        form = RatingsForm()

    context = {
        'ratings': ratings,
        'post': response,
        'form' : form,
        'rated': rated
    }

    return render(request, 'awards/detail.html', context)

def delete(request,pk):
    url = f'http://127.0.0.1:8000/postDelete/{pk}/'
    res = requests.delete(url)
    print(res)
    messages.success(request, 'project deleted successfully!')
    return redirect('home')

def create(request):
    url = f'http://127.0.0.1:8000/postCreate/'
    res = requests.delete(url)
    print(res)
    messages.success(request, 'project deleted successfully!')
    return redirect('home')
