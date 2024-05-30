from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']

class AddQuestionsForm(ModelForm):
    class Meta:
        model = QuizModel
        fields = "__all__"