from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.meme_list, name='meme_list'),
    path('meme_detail/<int:meme_id>/', views.meme_detail, name='meme_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)