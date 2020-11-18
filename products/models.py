from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    category = models.CharField(max_length=254, null=True, blank=True)
    sub_categories = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    url1 = models.URLField(max_length=1024, null=True, blank=True)
    color1 = models.CharField(max_length=254, null=True, blank=True)
    url2 = models.URLField(max_length=1024, null=True, blank=True)
    color2 = models.CharField(max_length=254, null=True, blank=True)
    url3 = models.URLField(max_length=1024, null=True, blank=True)
    color3 = models.CharField(max_length=254, null=True, blank=True)
    url4 = models.URLField(max_length=1024, null=True, blank=True)
    color4 = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
        