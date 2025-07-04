# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comment  # Importe o modelo Comment


class UserRegisterForm(UserCreationForm):
    # ... (código existente) ...
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Deixe seu comentário aqui...', 'class': 'form-control'}),
        }