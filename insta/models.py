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

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 60)
    image_caption = models.CharField(max_length=60)
    profile = models.ForeignKey(User)
    comments = models.CharField(max_length = 100)
    likes = models.ManyToManyField(User, related_name= 'likes', blank = True)

    @property
    def all_comments(self):
        return self.comment.all()
    
   

class CommentForm(models.Model):
    comment = models.CharField(max_length=250)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,related_name='comment')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment')
    
    def __str__(self):
        return self.comment

