from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from pyuploadcare.dj.forms import ImageField
from awards.models import Post, Ratings

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']
        
class PostForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description', 'technologies',)

        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ['design', 'usability', 'content']
 