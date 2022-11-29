from django.forms import ModelForm
from .models import Article, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['author','slug']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['owner','article']

        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Username',
                }), 
            'email': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Email',
                }), 
            'password1': forms.PasswordInput(attrs={
                        'placeholder':'Enter Password',
                }), 
            'password2': forms.PasswordInput(attrs={
                        'placeholder':'confirm Password2',
                }), 

        }

    