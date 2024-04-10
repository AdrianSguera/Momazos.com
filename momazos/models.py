from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Meme(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='memes/')

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)