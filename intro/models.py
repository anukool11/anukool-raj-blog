#python manage.py  makemigrations 
#python manage.py migrate
#python manage.py createsuperuser 
from django.db import models
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    bookid = models.IntegerField(primary_key = True)
    status = models.IntegerField(default=0)
    link = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    article_no = models.IntegerField(primary_key = True)
    title = models.TextField()
    tag = models.CharField(max_length=200)
    articletext = HTMLField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    pinned = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class RecommendationList(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)

