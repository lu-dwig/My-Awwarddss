# from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.CharField(max_length=500)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    
    def __str__(self, ):
        return  f'{self.user.username}Profile' 

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height >300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        
        

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, created, **kwargs):
        instance.profile.save()
        
        
