from django.contrib import admin
from accounts.models import Shopper
from articles.models import Category

admin.site.register(Shopper)


admin.site.register(Category)