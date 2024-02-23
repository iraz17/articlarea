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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from articles.views import articles_index, articles_detail, add_to_cart, cart, delete_cart
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("pages.urls")),
    path('signup/', include("accounts.urls")),
    path('login/', include("accounts.urls")),
    path('logout_user/', include("accounts.urls")),
    path('articles/', include("articles.urls")),
    path('cart/', include("articles.urls")),
    path('cart/delete', delete_cart, name='delete_cart'),
    path("articles/<str:slug>/", articles_detail, name="articles"),
    path("articles/<str:slug>/add_to_cart/", add_to_cart, name="add_to_cart"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
