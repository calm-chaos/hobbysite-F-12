from django.contrib import admin

from .models import Commission, Comment

class CommentInlineAdmin(admin.TabularInline):
    model = Comment

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [CommentInlineAdmin,]

admin.site.register(Commission, CommissionAdmin)

# Register your models here.
