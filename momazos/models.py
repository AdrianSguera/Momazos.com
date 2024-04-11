from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Meme(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='memes/')
    likes = models.ManyToManyField(User, related_name='liked_memes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_memes', blank=True)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)

class Comment(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
