
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from articles.models import Articles, Cart, Order

def articles_index(request):
    articles = Articles.objects.all()
    return render(request, "articles/articles_index.html", context={"articles": articles})

def articles_detail(request, slug):
    articles = get_object_or_404(Articles, slug=slug)
    
    return render(request, "articles/articles_detail.html", context={"articles": articles})

def add_to_cart(request, slug):
    user = request.user
    articles = get_object_or_404(Articles, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered = False, articles=articles)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    return redirect(reverse("articles", kwargs={"slug":slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'articles/cart.html', context={"orders":cart.orders.all()})

def delete_cart(request):
    cart = request.user.cart
    if cart:
        
        cart.delete()
    return redirect('home')