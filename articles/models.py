
from django.urls import reverse
from django.db import models
from django.conf import settings
from category.models import Category
from django.utils.text import slugify

class Articles(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    image = models.FileField(upload_to="articles_images/", blank=True, null=True)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True, max_length=128)
    composition = models.TextField(default='')
    date_added = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default= True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def search_by_category(cls, category_name):
        return Articles.objects.filter(category__name__icontains=category_name)  
      
    def get_absolute_url(self):
        return reverse('articles_detail', kwargs={'category_slug': self.category.slug, 'articles_slug': self.slug})

