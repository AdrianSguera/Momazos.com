from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.meme_list, name='meme_list'),
    path('meme_detail/<int:meme_id>/', views.meme_detail, name='meme_detail'),
    path('login/', views.login_view, name='login'),
    path('user_settings/', views.settings_view, name='user_settings'),
    path('logout/', views.logout_view, name='logout'),
    path('new_meme/', views.new_meme, name='new_meme'),
    path('new_username/', views.new_username, name='new_username'),
    path('new_password/', views.new_password, name='new_password'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('register/', views.register_view, name='register'),
    path('delete_comment/<int:comment_id>/<int:meme_id>/', views.delete_comment, name='delete_comment'),
    path('like/<int:meme_id>/', views.like_meme, name='like_meme'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)