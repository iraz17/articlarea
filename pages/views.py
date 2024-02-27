from django.shortcuts import render
from articles.models import Category, Articles


def home(request):
    return render(request, "pages/home.html")



def search_view(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    articles = Articles.objects.all()

    if query:
        articles = articles.filter(title__icontains=query)

    if category:
        articles = articles.filter(category__name=category)
    # Votre code existant pour la recherche

    categories = Category.objects.all()
    
    context = {
        'articles': articles,
        'query': query,
        'category': category,
        'categories': categories  # Passer les catégories au contexte
    }
    return render(request, 'search_results.html', context)