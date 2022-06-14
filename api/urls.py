from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name='api-overview'),
    path('postList/',views.postList, name="post-list"),
    path('postDetail/<str:pk>/',views.postDetail, name="post-detail"),
    path('postCreate/',views.postCreate, name="post-create"),
    path('postUpdate/<str:pk>/',views.postUpdate, name="post-update"),
    path('postDelete/<str:pk>/',views.postDelete, name="post-delet"),
    
]