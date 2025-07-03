# blog/views.py

from django.shortcuts import render, redirect  # Importe redirect
# Importe messages para exibir mensagens de sucesso/erro
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # Para proteger views
# Importa as views de autenticação do Django
from django.contrib.auth import views as auth_views

from .models import Post
from .forms import UserRegisterForm  # Importa seu formulário de registro


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Sobre'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Mensagem de sucesso que será exibida após o registro
            messages.success(
                request, f'Conta criada para {username}! Você já pode fazer login.')
            return redirect('login')  # Redireciona para a página de login
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form, 'title': 'Registrar'})

# As views de login/logout do Django já fazem todo o trabalho, então não precisamos escrevê-las.
# Apenas vamos conectá-las nas URLs.
