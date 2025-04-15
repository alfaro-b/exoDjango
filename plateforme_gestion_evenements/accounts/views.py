from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from .forms import UserRegisterForm

class HomeView(TemplateView):
    template_name = 'accounts/home.html'

    def get_context_data(self, **kwargs):
        contexte = super().get_context_data(**kwargs)
        return contexte
    
class SignUpView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response