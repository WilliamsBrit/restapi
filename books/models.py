from django.db import models

# Create your models here.
class Post(models.Model): # A Blog has a title, author, and body.
        title = models.CharField(max_length=200) 
