from rest_framework import serializers
from awards.models import Post
from users.models import Profile
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'description', 'technologies', 'image', 'date', 'user']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'image', 'bio', 'location', 'contact']

