from django.urls import path
from . import views

app_name='salutation'

urlpatterns = [
    # path('', views.salutation_home, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('bonjour/', views.bonjour_vue, name='bonjour'),
    path('au_revoir/', views.au_revoir_vue, name='au_revoir'),
    path('ajouter_article/', views.ajouter_article, name='ajouter'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
