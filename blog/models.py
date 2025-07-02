# blog/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # Para o autor do post

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Um post tem um autor

    def __str__(self):
        return self.title