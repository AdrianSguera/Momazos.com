from django.shortcuts import get_object_or_404, render, redirect
from .models import Meme, Comment
from django.utils import timezone
from .forms import CommentForm, NewUsername, CustomPasswordChangeForm, RegisterForm, MemeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

def meme_list(request):
    memes = Meme.objects.filter(date__lte=timezone.now()).order_by('-date')
    return render(request, 'momazos/meme_list.html', {'memes' : memes})

def meme_detail(request, meme_id):
    meme = get_object_or_404(Meme, pk=meme_id)
    comments = Comment.objects.filter(meme=meme, date__lte=timezone.now()).order_by('-date')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.meme = meme
            comment.date = timezone.now()
            comment.author = request.user
            comment.save()
            return redirect('meme_detail', meme_id=meme_id)
    else:
        form = CommentForm()

    return render(request, 'momazos/meme_detail.html', {'meme': meme, 'comments' : comments, 'form' : form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('meme_list')
    else:
        form = AuthenticationForm()
    return render(request, 'momazos/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('meme_list')

@login_required
def settings_view(request):
    return render(request, 'momazos/settings.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'momazos/register.html', {'form': form})

def new_meme(request):
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            meme = form.save(commit=False)
            meme.author = request.user
            meme.date = timezone.now()
            meme.save()
            return redirect('meme_list')
    else:
        form = MemeForm()
    return render(request, 'momazos/new_meme.html', {'form': form})

@login_required
def new_username(request):
    if request.method == 'POST':
        form = NewUsername(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your username was successfully updated!')
            return redirect('user_settings')
    else:
        form = NewUsername(instance=request.user)
    return render(request, 'momazos/new_username.html', {'form': form})

@login_required
def new_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'momazos/new_password.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.is_active = False
        request.user.save()
        return redirect('meme_list')
    else:
        return redirect('meme_list')
    
def delete_comment(request, comment_id, meme_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('meme_detail', meme_id=meme_id)

def like_meme(request, meme_id):
    meme = get_object_or_404(Meme, pk=meme_id)
    if request.user.is_authenticated:
        if request.user in meme.likes.all():
            meme.likes.remove(request.user)
            meme.likes_count -= 1
            liked = False
        else:
            meme.likes.add(request.user)
            meme.likes_count += 1
            liked = True
        meme.save()
        return JsonResponse({'likes_count': meme.likes_count, 'liked': liked})
    else:
        return JsonResponse({'error': 'User not authenticated'})

def dislike_meme(request, meme_id):
    meme = get_object_or_404(Meme, pk=meme_id)
    if request.user.is_authenticated:
        if request.user in meme.dislikes.all():
            meme.dislikes.remove(request.user)
            meme.dislikes_count -= 1
            disliked = False
        else:
            meme.dislikes.add(request.user)
            meme.dislikes_count += 1
            disliked = True
        meme.save()
        return JsonResponse({'dislikes_count': meme.dislikes_count, 'disliked': disliked})
    else:
        return JsonResponse({'error': 'User not authenticated'})
