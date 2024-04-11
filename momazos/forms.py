from django import forms
from .models import Comment, Meme
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class NewUsername(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['image', 'description']
        labels = {
            'image': 'Choose file:',
            'description': 'Description:',
        }
        
