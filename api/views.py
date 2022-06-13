from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'PostList':'/post-list/',
        'Detail View': '/post-detail/<str:pk>/',
        'Create': '/post-create/',
        'Update': '/post-update/<str:pk>/',
        'Delete': '/post-delete/<str:pk>/',
    }
    return Response(api_urls)
