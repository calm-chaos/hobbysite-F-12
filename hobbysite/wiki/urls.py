from django.urls import path

from .views import *

urlpatterns = [
    path("articles", articles, name="article-library"),
    path("article/<int:pk>", article, name="article"),
    path("articles/add", article_create, name="article-create"),
    path("article/<int:pk>/edit", article_update, name="article-update"),
]

app_name = "wiki"
