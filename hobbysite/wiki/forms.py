from django import forms

from .models import *


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "category", "entry", "header_image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry"]
        labels = {"entry": ""}


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "category", "entry", "header_image"]
