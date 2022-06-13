from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name='api-overview'),
    path('post-list/',views.postList, name="post-list"),
    
    
]