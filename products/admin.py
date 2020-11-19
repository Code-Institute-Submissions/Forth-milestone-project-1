from django.contrib import admin
from .models import database

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'category',
        'sub_categories',
        'price',
    )

    ordering = ('brand',)
admin.site.register(database, ProductAdmin)
