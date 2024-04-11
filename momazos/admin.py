from django.contrib import admin
from .models import Meme, Like, Dislike, Comment

admin.site.register(Meme)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Comment)