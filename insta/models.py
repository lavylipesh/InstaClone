from django.db import models
import datetime as dt

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='static/', blank = 'true')
    bio = models.TextField(default="")

class Image(models.Model):
  
    image_name = models.CharField(max_length = 60)
    image_caption = models.CharField(max_length=60)
    profile = models.ForeignKey(Profile)
    pub_date = models.DateTimeField(auto_now_add=True)
      image = models.ImageField(upload_to = 'images/')
    
   
   