from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .models import Comment
from events.models import Event
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/ajouter_comment.html'
    success_url = reverse_lazy('events:liste_events')

    def form_valid(self, form):
        event = get_object_or_404(Event, pk=self.kwargs['event_pk'])
        form.instance.auteur = self.request.user
        form.instance.evenement = event
        response = super().form_valid(form)
        return response
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comments/supprimer_comment.html'
    context_object_name = 'comment'
    success_url = reverse_lazy('events:liste_events')

    def test_func(self):
        obj = self.get_object()
        return obj.auteur == self.request.user