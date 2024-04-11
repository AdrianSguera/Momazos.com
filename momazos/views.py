from django.shortcuts import get_object_or_404, render, redirect
from .models import Meme, Comment
from django.utils import timezone
from .forms import CommentForm

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
