from django.db import models
import datetime as dt

class Profile(models.Model):
    name = models.CharField(max_length=60)
    profile_pic = models.ImageField(upload_to='static/')
    bio = models.TextField(default="")
    
    @classmethod
    def search_by_name(cls,search_term):
        insta = cls.objects.filter(name_icontains=search_term)
        return insta

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 60)
    image_caption = models.CharField(max_length=60)
    profile = models.ForeignKey(Profile)
    pub_date = models.DateTimeField(auto_now_add=True)
    
class InstaRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()  
   