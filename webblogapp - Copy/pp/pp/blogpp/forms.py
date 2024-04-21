from django import forms
from .models import Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['author', 'content']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter your email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)