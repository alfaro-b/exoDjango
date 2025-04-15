from django.db import models
from django.contrib import admin

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()

    def __str__(self):
        return self.titre
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "contenu")
    list_filter = ("titre",)
