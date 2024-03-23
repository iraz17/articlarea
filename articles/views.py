
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from articles.models import Articles, Category
from carts.models import CartItem
from django.db.models import Q
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def articles_index(request, category_slug=None):
    categories = None
    articles = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        articles = Articles.objects.filter(category=categories, is_available=True)
        paginator = Paginator(articles, 6)
        page = request.GET.get('page')
        paged_articles = paginator.get_page(page)
        article_count = articles.count()
    else:
        articles = Articles.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(articles, 6)
        page = request.GET.get('page')
        paged_articles = paginator.get_page(page)
        article_count = articles.count()

    return render(request, "articles/articles_index.html", context={"articles": paged_articles, 'article_count': article_count})

def delete_article(request, slug):
    try:
        article = Articles.objects.get(slug=slug)
        article.delete()
        messages.success(request, "L'article a été supprimé avec succès.")
    except Articles.DoesNotExist:
        messages.error(request, "L'article que vous essayez de supprimer n'existe pas.")
    
    return redirect('cart') 

def articles_detail(request, category_slug, articles_slug):
    try:
        single_articles = Articles.objects.get(category__slug=category_slug, slug=articles_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), articles=single_articles).exists()
        
    except Exception as e:
        raise e
    
    return render(request, "articles/articles_detail.html", context={'single_articles': single_articles, 'in_cart':in_cart})

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            articles = Articles.objects.order_by('-created_date').filter(Q(description__icontains=keyword)| Q(title__icontains=keyword))
            article_count= articles.count()
    return render(request, "articles/articles_index.html", context = { 'articles': articles, 'article_count': article_count})

