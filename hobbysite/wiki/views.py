from django.shortcuts import render

from .models import Article, ArticleCategory


def articles(request):
    ctx = {"library": Article.objects.all()}

    return render(request, "wiki_list.html", ctx)


def article(request, pk):
    article = Article.objects.get(pk=pk)
    other_articles = Article.objects.filter(category=article.category).exclude(pk=pk)[
        :2
    ]

    ctx = {
        "title": article.title,
        "entry": article.entry,
        "created_on": article.created_on,
        "updated_on": article.updated_on,
        "category": article.category,
        "other_articles": other_articles,
    }

    return render(request, "wiki_detail.html", ctx)
