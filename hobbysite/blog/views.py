from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import *
from .models import *


def blog_list(request):
    if request.user.is_authenticated:
        user_articles = Article.objects.filter(author=request.user.profile)
        other_articles = Article.objects.exclude(author=request.user.profile)
        user_categories = ArticleCategory.objects.filter(
            articles__in=user_articles
        ).distinct()
        all_categories = ArticleCategory.objects.all()
        ctx = {
            "auth_user": request.user.profile,
            "user_articles": user_articles,
            "other_articles": other_articles,
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

    return render(request, "blog_list.html", ctx)


def blog_detail(request, pk):
    article = Article.objects.get(pk=pk)
    user_other_articles = Article.objects.filter(author=article.author).exclude(pk=pk)[
        :2
    ]
    comments = Comment.objects.filter(article=article).order_by("-created_on")

    form = BlogCommentForm()
    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.profile
            comment.article = article
            comment.save()

    ctx = {
        "title": article.title,
        "author": article.author,
        "category": article.category,
        "entry": article.entry,
        "image": article.headerImage,
        "created_on": article.created_on,
        "updated_on": article.updated_on,
        "comments": comments,
        "form": form,
        "user_other_articles": user_other_articles,
    }

    return render(request, "blog_detail.html", ctx)


@login_required
def blog_create(request):
    if request.method == "POST":
        form = BlogCreateForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user.profile
            article.created_on = timezone.now()
            article.updated_on = timezone.now()
            article.save()
            return redirect("blog:articles")
    else:
        form = BlogCreateForm()
    return render(request, "blog_create.html", {"form": form})


@login_required
def blog_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = BlogUpdateForm(request.POST or None, request.FILES, instance=article)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("blog:article-detail", pk=pk)
    else:
        form = BlogUpdateForm(instance=article)
    return render(request, "blog_update.html", {"form": form, "article": article})


def blog_gallery(request):
    articleImages = Article.objects.all()

    ctx = {"articles": articleImages}
    return render(request, "blog_gallery.html", ctx)
