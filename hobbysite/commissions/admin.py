from django.contrib import admin

from .models import Commission, Job, JobApplication

class JobInlineAdmin(admin.TabularInline):
    model = Job

class JobApplicationInlineAdmin(admin.TabularInline):
    model = JobApplication

# class CommentInlineAdmin(admin.TabularInline):
#     model = JobApplication

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [JobInlineAdmin,]

class JobApplicationAdmin(admin.ModelAdmin):
    model = Job
    inlines = [JobApplicationInlineAdmin,]

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobApplicationAdmin)

# Register your models here.