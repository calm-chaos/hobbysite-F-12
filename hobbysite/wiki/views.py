from django.shortcuts import render

from .models import Article, ArticleCategory


def articles(request):
    ctx = {"library": Article.objects.all()}

    return render(request, "articles.html", ctx)


def article(request, pk):
    article = Article.objects.get(pk=pk)

    ctx = {
        "title": article.title,
        "entry": article.entry,
        "created_on": article.created_on,
        "updated_on": article.updated_on,
        "category": article.category,
    }

    return render(request, "article.html", ctx)
