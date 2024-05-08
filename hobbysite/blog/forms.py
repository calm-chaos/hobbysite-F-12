from django import forms
from .models import *


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "category",
            "entry",
            "headerImage",
        ]


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "entry",
        ]


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "category",
            "entry",
            "headerImage",
        ]
