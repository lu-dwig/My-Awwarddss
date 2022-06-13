from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    


