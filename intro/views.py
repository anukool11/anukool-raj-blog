from django.shortcuts import render, redirect
from .models import Book, Article
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import HttpResponseRedirect
from .models import Book, Article, RecommendationList
from django.db.models import Avg

def index(request):
    return redirect('/home')

def home(request):
    return render(request, "intro/home.html",{
        "Article": Article.objects.filter(pinned=1)
    })

def books(request):
    return render(request, "intro/books.html", {
        "Book": Book.objects.all(),
        "RecommendationList": RecommendationList.objects.all()
    })

def articles(request):
    return render(request, "intro/articles.html", {
        "Article": Article.objects.all()
    })

def readarticle(request, article_no):
    article=Article.objects.get(article_no=article_no)
    return render(request, "intro/readarticle.html", {
        "article":article 
    })

