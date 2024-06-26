# Generated by Django 5.0.4 on 2024-04-11 19:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('momazos', '0004_auto_20240411_1546'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='meme',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AddField(
            model_name='meme',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='disliked_memes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meme',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_memes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='meme',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Dislike',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
