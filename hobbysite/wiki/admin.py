from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "created_on", "updated_on", "entry"]
    list_filter = ["category"]
    search_fields = ["title", "entry"]


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "author", "created_on", "updated_on", "entry"]
    list_filter = ["article"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
