# admin.py

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'qte_stock', 'image', 'view_on_site')

    def view_on_site(self, obj):
        return obj.get_absolute_url()

    view_on_site.short_description = 'View on site'
