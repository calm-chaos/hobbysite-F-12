from django import forms

from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "category", "entry", "header_image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry"]
        labels = {"entry": ""}
