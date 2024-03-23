from django.contrib import admin
from .models import Articles

class AdminArticles(admin.ModelAdmin):
    list_display = ('category', 'title', 'description', 'price', 'stock', 'composition', 'date_added', 'created_date', 'modified_date')
    prepopulated_field = {'slug': ('title',)}
    
admin.site.register(Articles, AdminArticles)


