# blog/views.py

# Importar get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
# from django.views.generic import DetailView # Não precisamos mais desta para a página de detalhes
from .models import Post, Comment  # Importar Comment
from .forms import UserRegisterForm, CommentForm  # Importar CommentForm


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    # A view home não vai mais processar o formulário de comentários diretamente,
    # mas precisará passar uma instância de formulário para cada post.
    # Isso será feito no template.
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Sobre'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Conta criada para {username}! Você já pode fazer login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form, 'title': 'Registrar'})


@login_required  # Garante que apenas usuários logados podem acessar esta view
def add_comment_to_post(request, pk):  # Recebe o ID (pk) do post
    # Busca o post, ou retorna 404 se não encontrar
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Não salva ainda
            comment.post = post              # Associa ao post atual
            comment.author = request.user    # Associa ao usuário logado
            comment.save()
            messages.success(request, 'Seu comentário foi adicionado!')
            # Redireciona de volta para a página inicial
            return redirect('blog-home')
        else:
            messages.error(
                request, 'Erro ao adicionar comentário. Verifique o formulário.')
            # Se houver erro, redireciona de volta para a home para exibir a mensagem de erro
            return redirect('blog-home')
    else:
        # Se for um GET request para esta URL (o que não deve acontecer muito),
        # apenas redireciona de volta para a home.
        return redirect('blog-home')
