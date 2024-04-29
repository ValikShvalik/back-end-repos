from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password')  # Добавьте дополнительные поля, если необходимо


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
