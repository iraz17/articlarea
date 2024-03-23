from django.shortcuts import get_object_or_404, redirect, render
from .models import Articles, Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist



def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, articles_id):
    articles = Articles.objects.get(id=articles_id)
    try:
        cart = Cart.objects.get(cart_id= _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()
    
    try : 
        cart_item = CartItem.objects.get(articles=articles, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            articles = articles,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    
    return redirect('cart')

def remove_cart(request, articles_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    articles = get_object_or_404(Articles, id=articles_id)
    cart_item = CartItem.objects.get(articles=articles, cart = cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request, articles_id):
    cart = Cart.objects.get(cart_id= _cart_id(request))
    articles = get_object_or_404(Articles, id=articles_id)
    cart_item = CartItem.objects.get(articles = articles, cart = cart)
    cart_item.delete()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total +=(cart_item.articles.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax

    except ObjectDoesNotExist:
        pass
    
    return render(request,'cart/cart.html', context={'total':total, 'quantity':quantity, 'cart_items':cart_items, 'tax': tax, 'grand_total': grand_total, })


