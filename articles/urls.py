from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles_index, name='articles_index'),
    path('cart/', views.cart, name='cart'),
    
]