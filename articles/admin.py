from django.contrib import admin
from articles.models import Articles, Order, Cart

class ArticlesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Order)
admin.site.register(Cart)


