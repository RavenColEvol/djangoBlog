from django.db import models

# Create your models here.
class BlogPosts(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    publish = models.TimeField(auto_now=True)


    def __str__(self):
        return self.title
    
class BlogUser(models.Model):
    username =  models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username