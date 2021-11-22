from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import CustomUser
class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username', 'password1', 'password2', 'nickname', 'university']