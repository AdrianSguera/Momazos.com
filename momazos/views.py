from django.shortcuts import get_object_or_404, render
from .models import Meme
from django.utils import timezone

def meme_list(request):
    memes = Meme.objects.filter(date__lte=timezone.now()).order_by('-date')
    return render(request, 'momazos/meme_list.html', {'memes' : memes})

def meme_detail(request, meme_id):
    meme = get_object_or_404(Meme, pk=meme_id)
    return render(request, 'momazos/meme_detail.html', {'meme': meme})
