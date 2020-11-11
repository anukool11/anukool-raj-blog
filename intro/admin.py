from django.contrib import admin
from .models import Book, Article, RecommendationList

# Register your models here.

admin.site.register(Book)
admin.site.register(Article)
admin.site.register(RecommendationList)