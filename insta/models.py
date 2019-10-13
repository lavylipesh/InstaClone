from django.db import models

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='static/', blank = 'true')
    bio = models.TextField(default="")

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 60)
    image_caption = models.CharField(max_length=60)
    profile = models.ForeignKey(name = 'profile')
    
    
   
   