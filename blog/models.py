# blog/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    from django.urls import reverse

    def get_absolute_url(self):
        # Esta função ainda é útil, mesmo que não haja uma página de detalhes dedicada,
        # pode ser usada para links em outros lugares ou no admin.
        # Vamos usar 'post-detail' como um nome de URL genérico para um post específico,
        # mesmo que não seja uma página de detalhes completa.
        return reverse('post-detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return f'Comentário de {self.author.username} em {self.post.title[:50]}'
