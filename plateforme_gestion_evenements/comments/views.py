from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .models import Comment, Event
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/ajouter_comment.html'
    success_url = reverse_lazy('events:liste_events')

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        form.instance.evenement = Event.titre
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