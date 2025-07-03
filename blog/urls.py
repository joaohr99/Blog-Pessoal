# blog/urls.py

from django.urls import path
from . import views
# Importe as views de autenticação
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('register/', views.register, name='register'),  # URL para registro

    # URLs para Login e Logout (usando as views padrão do Django)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]
