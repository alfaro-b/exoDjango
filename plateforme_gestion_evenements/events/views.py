from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event
from .forms import EventForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/liste_events.html'
    ordering = ['-date']
    paginate_by = 5


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/detail_event.html'
    context_object_name = 'event'
   # Utilisation du slug pour trouver l'article dans l'URL
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/ajouter_event.html'
    success_url = reverse_lazy('events:liste_events')

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        response = super().form_valid(form)
        return response
    
class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    template_name = 'events/modifier_event.html'
    context_object_name = 'event'
    form_class = EventForm
    success_url = reverse_lazy('events:liste_events')

    def test_func(self):
        obj = self.get_object()
        return obj.auteur == self.request.user


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/supprimer_event.html'
    context_object_name = 'event'
    success_url = reverse_lazy('events:liste_events')

    def test_func(self):
        obj = self.get_object()
        return obj.auteur == self.request.user

