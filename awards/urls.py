from django.urls import path
from .views import PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('search/', views.searchPhoto, name='search'),
    path('post-detail/<str:pk>/', views.detail, name='post-detail'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('new/', PostCreateView.as_view(), name='post-new'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]