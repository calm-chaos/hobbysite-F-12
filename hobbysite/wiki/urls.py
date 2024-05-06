from django.urls import path

from .views import *

urlpatterns = [
    path("articles", articles, name="article-library"),
    path("article/<int:pk>", article, name="article"),
    path("article/add", article_create, name="article-create"),
    path("article/<int:pk>/edit", article_update, name="article-update"),
    path("gallery", gallery, name="gallery"),
]

app_name = "wiki"
