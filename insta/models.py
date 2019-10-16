from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='images/')
    bio = models.TextField(default="")

    def __str__(self):
        return f'{self.user.username}Profile'
    @classmethod
    def search_by_user(cls,search_term):
      user = cls.objects.filter(user__username__icontains=search_term)
      return user   
    

class Comment(models.Model):
    comment = models.CharField(max_length = 80) 
    
    def __str__(self):
        return self.comment

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 60)
    image_caption = models.CharField(max_length=60)
    profile = models.ForeignKey(Profile)
    comment = models.ForeignKey(Comment)
    likes = models.ManyToManyField(User, related_name= 'likes', blank = True)

