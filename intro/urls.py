from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("books", views.books, name="books"),
    path("articles", views.articles, name="articles"),
    path("articles/<int:article_no>", views.readarticle, name="readarticle"),
]