from django.urls import path
from . import views
from .views import search_view

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', search_view, name='search'),
]