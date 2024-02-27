from django import forms
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Articles(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default='none')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to="articles_images/", blank=True, null=True)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True, max_length=128)
    composition = models.TextField(default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def search_by_category(cls, category_name):
        return Articles.objects.filter(category__name__icontains=category_name)
    def get_absolute_url(self):
        return reverse('articles_detail', kwargs={'slug': self.slug})
    
# Article (Order)
"""
- Utilisateur
- Produit
- Quantité
- Commande ou non

"""
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.articles.title} ({self.quantity})"
    
    
#Panier(Cart)
"""
- Utilisateur
- Articles
- Commandé ou non
- Date de la commande
"""

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    
    

    def __str__(self):
        return self.user.username
    
    def delete(self, *args, **kwargs):
        

        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()
        
        self.orders.clear()
        super().delete(*args, **kwargs)


class CartForm(forms.Form):
    class Meta:
        model = Order
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1}),
        }
        
    def __int__(self, *args, **kwargs):
        self.orders = kwargs.pop('orders')
        super(CartForm, self).__init__(*args, **kwargs)

        for order in self.orders:
            self.fields['quantity_%s' % order.id] = forms.IntegerField(min_value=0, max_value=order.quantity, initial=0)