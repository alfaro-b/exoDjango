from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import TemplateView
from .forms import ArticleForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

# def salutation_home(request):
#     return render(request, 'salutation/home.html')

class HomeView(TemplateView):
    template_name = 'salutation/home.html'

    def get_context_data(self, **kwargs):
        contexte = super().get_context_data(**kwargs)
        # contexte["user"] = "pierpoljak"
        return contexte

def bonjour_vue(request):
    return render(request, 'salutation/bonjour.html')

def au_revoir_vue(request):
    return render(request, 'salutation/au_revoir.html')

def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre en base
            return redirect('salutation:home')  # Redirige après soumission
            # return redirect(reverse('salutation:home'))  # Redirige après soumission

    else:
        form = ArticleForm()
        return render(request, 'salutation/ajouter_article.html', {'form': form}) 

@login_required
def dashboard(request):
    utilisateur = request.user
    return render(request, 'salutation/dashboard.html', {'utilisateur': utilisateur})
