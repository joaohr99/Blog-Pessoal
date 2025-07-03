# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm # Importa o formulário de criação de usuário do Django

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Adiciona um campo de e-mail ao formulário de registro

    class Meta(UserCreationForm.Meta):
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields + ('email',) # Inclui o campo de e-mail nos campos