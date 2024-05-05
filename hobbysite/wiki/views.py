from django.shortcuts import render

from .models import Article, ArticleCategory


def articles(request):
    if request.user.is_authenticated:
        user_articles = Article.objects.filter(author=request.user.profile)
        all_other_articles = Article.objects.exclude(author=request.user.profile)
        user_categories = ArticleCategory.objects.filter(
            articles__in=user_articles
        ).distinct()
        all_categories = ArticleCategory.objects.all()
        ctx = {
            "logged_user": request.user.profile,
            "user_articles": user_articles,
            "all_other_articles": all_other_articles,
            "user_categories": user_categories,
            "all_categories": all_categories,
        }
    else:
        all_articles = Article.objects.all()
        all_categories = ArticleCategory.objects.all()
        ctx = {
            "all_articles": all_articles,
            "all_categories": all_categories,
        }

    return render(request, "wiki_list.html", ctx)


def article(request, pk):
    article = Article.objects.get(pk=pk)
    other_articles = Article.objects.filter(category=article.category).exclude(pk=pk)[
        :2
    ]

    ctx = {
        "title": article.title,
        "author": article.author,
        "entry": article.entry,
        "image": article.header_image,
        "created_on": article.created_on,
        "updated_on": article.updated_on,
        "category": article.category,
        "other_articles": other_articles,
    }

    return render(request, "wiki_detail.html", ctx)
