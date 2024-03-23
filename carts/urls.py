from django.urls import path
from . import views

urlpatterns =[
    path('', views.cart, name='cart'),
    path('add_cart/<int:articles_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:articles_id>', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:articles_id>', views.remove_cart_item, name='remove_car_item'),
]
 ###path('cart/delete_article/<slug:slug>/', views.delete_article, name='delete_article'),
 ###   path('cart/delete/', views.delete_cart, name='delete_cart'),
  ###  path('<slug:slug>/add_to_cart/', views.add_to_cart, name='add_to_cart'),