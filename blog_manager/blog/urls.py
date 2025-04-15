from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('liste_articles/', views.liste_articles, name='liste_articles'),
    path('detail_article/<slug:slug>', views.detail_article, name='detail_article'),
    path('ajouter_article/', views.ajouter_article, name='ajouter'),
]
