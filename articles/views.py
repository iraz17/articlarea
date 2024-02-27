
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from articles.models import Articles, Cart, CartForm, Order, Category
from .forms import CartForm

def articles_index(request):
    articles = Articles.objects.all()
    return render(request, "articles/articles_index.html", context={"articles": articles})

def delete_article(request, slug):
    try:
        article = Articles.objects.get(slug=slug)
        article.delete()
        messages.success(request, "L'article a été supprimé avec succès.")
    except Articles.DoesNotExist:
        messages.error(request, "L'article que vous essayez de supprimer n'existe pas.")
    
    return redirect('cart') 

def articles_detail(request, slug):
    article = get_object_or_404(Articles, slug=slug)
    
    category_name = request.GET.get('category', '')
    if category_name:
        category_articles = Articles.search_by_category(category_name)
    else:
        category_articles = None
        
    return render(request, "articles/articles_detail.html", context={"article": article, "category_articles": category_articles})

def add_to_cart(request, slug):
    user = request.user
    articles = get_object_or_404(Articles, slug=slug)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        if quantity > articles.stock:
            messages.error(request, "La quantité demandée dépasse la quantité en stock. ")
            return redirect(reverse("articles_detail", kwargs={"slug":slug}))
        cart, _ = Cart.objects.get_or_create(user=user)
        order, created = Order.objects.get_or_create(user=user, ordered=False, articles=articles)

        if created:
            order.quantity = quantity
            order.save()
            cart.orders.add(order)
            cart.save()
            messages.success(request, f"{quantity} {articles.title}(s) ajouté(s) au panier.")
        else:
            order.quantity += quantity
            order.save()
            messages.success(request, f"{quantity} {articles.title}(s) ajouté(s) au panier.")
    return redirect(reverse("articles_detail", kwargs={"slug":slug}))
    

def cart(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    orders = Order.objects.filter(user=user, ordered=False)
    
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            for order in orders:
                new_quantity = form.cleaned_data.get('quantity')
                if new_quantity == 0:
                    order.delete()
                else:
                    order.quantity = new_quantity
                    order.save()
            messages.success(request, "Quantités mises à jour avec succès.")
            return redirect(reverse('cart'))
    else:
        form = CartForm()

    remaining_quantities = {}
    for order in orders:
        remaining_quantities[order.id] = order.quantity - int(request.POST.get(str(order.id), order.quantity))

    return render(request, 'articles/cart.html', context={'orders': orders, 'form': form, 'remaining_quantities': remaining_quantities})

def delete_cart(request):
    cart = request.user.cart
    if cart:

        cart.delete()
    return redirect('home')

def search_view(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    articles = Articles.objects.all()

    if query:
        articles = articles.filter(title__icontains=query)

    if category:
        articles = articles.filter(category__name=category)

    if min_price:
        articles = articles.filter(price__gte=min_price)
    
    if max_price:
        articles = articles.filter(price__lte=max_price)
    
    categories = Category.objects.all()

    context = {
        'articles': articles,
        'query' : query,
        'category': category,
        'min_price': min_price,
        'max_price': max_price,
        'categories': categories
    }
    return render(request, 'search_results.html', context)