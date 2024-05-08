from django.urls import path
from .views import *

urlpatterns = [
    path("articles/", blog_list, name="articles"),
    path("article/<int:pk>/", blog_detail, name="article-detail"),
    path("article/add/", blog_create, name="create"),
    path("article/<int:pk>/edit", blog_update, name="edit"),
    path("gallery", blog_gallery, name="gallery"),
]

app_name = "blog"
