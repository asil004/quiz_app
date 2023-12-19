from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class AddQuestionForm(ModelForm):
    class Meta:
        model = QuesModel
        fields = "__all__"
