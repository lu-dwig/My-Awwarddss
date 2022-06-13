from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from awards.models import Post
from .serializers import PostSerializer
from awards.models import Post

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/post-list/',
        'Detail View': '/post-detail/<str:pk>/',
        'Create': '/post-create/',
        'Update': '/post-update/<str:pk>/',
        'Delete': '/post-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postDetail(request,pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def postUpdate(request, pk):
    posts = Post.objects.get(id=pk)
    
    serializer = PostSerializer(instance=posts, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)
