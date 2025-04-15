from django.db import models
from django.contrib import admin
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    titre = models.CharField(max_length=100, unique=True, )
    auteur = models.CharField(max_length=100)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True) # Pour des URLs lisibles

    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        # Générer automatiquement le slug à partir du titre
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "auteur", "contenu", "date")
    list_filter = ("date",)
