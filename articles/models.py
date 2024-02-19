from datetime import timezone
from django.db import models
from django.urls import reverse

from articlarea.settings import AUTH_USER_MODEL

class Articles(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to="articles_images/", blank=True, null=True)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    slug = models.SlugField(max_length=128)

    def __str__(self):
        return f"{self.title} ({self.stock})"
    
    def get_absolute_url(self):
        return reverse("articles", kwargs={"slug":self.slug})
    
# Article (Order)
"""
- Utilisateur
- Produit
- Quantité
- Commande ou non

"""
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
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
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    
    

    def __str__(self):
        return self.user.username
    
    def delete(self, *args, **kwargs):
        for order in self.order.all():
            order.order_date = timezone.now()
            order.save()
        
        self.orders.clear()
        super().delete(*args, **kwargs)