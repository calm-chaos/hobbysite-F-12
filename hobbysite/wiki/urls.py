from django.urls import path

from .views import article, articles

urlpatterns = [
    path("articles", articles, name="article-library"),
    path("article/<int:pk>", article, name="article"),
]

app_name = "wiki"
