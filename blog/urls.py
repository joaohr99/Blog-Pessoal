# blog/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# Remova: from blog.views import PostDetailView # Se você tinha isso, remova

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Remova esta linha se você a tinha para a PostDetailView:
    # path('post/<slug:slug>/', views.post_detail, name='post-detail'),

    # Nova URL para adicionar comentários
    path('post/<int:pk>/add_comment/',
         views.add_comment_to_post, name='add-comment'),
]
