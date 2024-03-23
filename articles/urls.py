from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles_index, name='articles_index'),
    path('category/<slug:category_slug>/', views.articles_index, name='articles_by_category'),
    path('category/<slug:category_slug>/<slug:articles_slug>/', views.articles_detail, name='articles_detail'),
    path('search/', views.search, name='search'),
]
