from django.urls import path
from . import views
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView

app_name='events'

urlpatterns = [
    path('liste_events/', EventListView.as_view(), name='liste_events'),
    path('detail_event/<slug:slug>', EventDetailView.as_view(), name='detail_event'),
    path('ajouter_event/', EventCreateView.as_view(), name='ajouter_event'),
    path('modifier_event/<slug:slug>', EventUpdateView.as_view(), name='modifier_event'),
    path('supprimer_event/<slug:slug>', EventDeleteView.as_view(), name='supprimer_event'),
]