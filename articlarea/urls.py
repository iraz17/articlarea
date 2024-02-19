"""
URL configuration for articlarea project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from articles.views import articles_index, articles_detail, add_to_cart, cart, delete_cart
from accounts.views import signup, logout_user, login_user
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('articles/', articles_index, name='articles_index'),
    path('cart/', cart, name='cart'),
    path('cart/delete', delete_cart, name='delete_cart'),
    path("articles/<str:slug>/", articles_detail, name="articles"),
    path("articles/<str:slug>/add_to_cart/", add_to_cart, name="add_to_cart"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
