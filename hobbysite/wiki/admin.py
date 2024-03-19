from django.contrib import admin

from .models import Article, ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "created_on", "updated_on"]
    list_filter = ["category"]
    search_fields = ["title", "entry"]


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
