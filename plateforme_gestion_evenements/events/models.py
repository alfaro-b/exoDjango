from django.db import models
from django.contrib import admin
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    lieu = models.CharField(max_length=100)
    capacite = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Pour des URLs lisibles
    auteur = models.ForeignKey(User, on_delete=models.CASCADE) # Si un utilisateur est supprimé, les évènements qu'il a créé seront aussi supprimés

    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        # Générer automatiquement le slug à partir du titre
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
    
class EventAdmin(admin.ModelAdmin):
    list_display = ("titre", "description", "date", "lieu", "capacite", "auteur")
    list_filter = ("date",)


