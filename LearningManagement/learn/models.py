from django.db import models
from django.contrib import auth
from django.utils import timezone

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

 
    def __str__(self):
        return "@{}".format(self.username)

class Article(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='member')
    name = models.CharField(max_length=400)
    text = models.TextField()
    
    
    def __str__(self):
        return self.name

class Book(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='user')
    name = models.CharField(max_length=400)
    description = models.TextField()
    publisher = models.TextField()
    rating = models.IntegerField()
    language = models.TextField()
    
    def __str__(self):
        return self.name