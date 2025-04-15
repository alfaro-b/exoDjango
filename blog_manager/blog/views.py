from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
from django.core.paginator import Paginator

def liste_articles(request):
    articles = Article.objects.all().order_by('-date')
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/liste_articles.html',{'page_obj': page_obj})

def detail_article(request,slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/detail_article.html',{'article' : article})


def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre en base
            messages.add_message(request, messages.INFO, 'L\'article a bien été ajouté.')
            return redirect('blog:liste_articles')  # Redirige après soumission
    else:
        form = ArticleForm()
        return render(request, 'blog/ajouter_article.html', {'form': form}) 
    
# Create your views here.
 