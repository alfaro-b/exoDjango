from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.
class Comment(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Event, on_delete=models.CASCADE)
    contenu = models.TextField()
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.evenement
    
class EventAdmin(admin.ModelAdmin):
    list_display = ("auteur", "evenement", "contenu", "date")
    list_filter = ("date",)