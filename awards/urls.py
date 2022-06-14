from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('search/', views.searchPhoto, name='search'),
    path('post-detail/<str:pk>/', views.detail, name='post-detail'),
    
]