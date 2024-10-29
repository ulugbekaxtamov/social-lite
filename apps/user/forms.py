from django.contrib.auth.forms import UserCreationForm
from apps.user.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'name', 'password1', 'password2')