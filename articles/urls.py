from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.articles_index, name='articles_index'),
    path('articles/<slug:slug>/', views.articles_detail, name='articles_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/deletearticles/<slug:slug>/', views.delete_article, name='delete_article'),
    path('cart/delete/', views.delete_cart, name='delete_cart'),
    path('<slug:slug>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
]
