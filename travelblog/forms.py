from .models import Comment
from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CustomSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
