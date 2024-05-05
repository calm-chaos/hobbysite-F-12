from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import *
from .models import *


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
    comments = Comment.objects.filter(article=article).order_by("-created_on")

    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.profile
            comment.article = article
            comment.save()
            return redirect("wiki:article", pk=pk)

    ctx = {
        "title": article.title,
        "author": article.author,
        "entry": article.entry,
        "image": article.header_image,
        "created_on": article.created_on,
        "updated_on": article.updated_on,
        "category": article.category,
        "other_articles": other_articles,
        "comments": comments,
        "form": form,
    }

    return render(request, "wiki_detail.html", ctx)


@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user.profile
            article.created_on = timezone.now()
            article.updated_on = timezone.now()
            article.save()
            return redirect("wiki:article-library")
    else:
        form = ArticleCreateForm()
    return render(request, "wiki_create.html", {"form": form})


@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleUpdateForm(request.POST or None, request.FILES, instance=article)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("wiki:article", pk=pk)
    else:
        form = ArticleUpdateForm(instance=article)
    return render(request, "wiki_update.html", {"form": form, "article": article})
