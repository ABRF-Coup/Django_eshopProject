
from django.utils import timezone
from django.db import models
from django.urls import reverse

from Shop.settings import AUTH_USER_MODEL

# Create your models here.
"""
Product:
-Nom
-Prix
-Quantite_Stock
-Description
-Image
"""

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.FloatField(default=0.0)
    qte_stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


#Order , Article voulu par le user
"""
-Utilisateur
-Produit
-Quantité
-Commandé ou non 
"""

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True,null=True)
    

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


# Panier (Cart)
"""
-Utilisateur
-Articles
-Commandé ou non
-Date de la commande
"""

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE) #Je pouvais aussi faire un ForeignKey en faisant user= models.ForeignKey(unique=True)
    orders = models.ManyToManyField(Order) #plusieurs articles peuvent etre ajoutés au panier
    

    def __str__(self):
        return self.user.username
    
    def delete(self,*args,**kwargs):

        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()



        super().delete(*args,**kwargs)