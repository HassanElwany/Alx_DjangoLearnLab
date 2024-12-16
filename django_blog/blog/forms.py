from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Comment, Post, Tag



class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        help_text="Tell us something about yourself (optional)."
    )
    profile_picture = forms.ImageField(
        required=False,
        help_text="Upload a profile picture (optional)."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile_picture']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'}),
        }