from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    sub_categories = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    url1 = models.URLField(max_length=1024)
    color1 = category = models.CharField(max_length=254)
    url2 = models.URLField(max_length=1024)
    color2 = category = models.CharField(max_length=254)
    url3 = models.URLField(max_length=1024)
    color3 = category = models.CharField(max_length=254)
    url4 = models.URLField(max_length=1024)
    color4 = category = models.CharField(max_length=254)

    def __str__(self):
        return self.product_name