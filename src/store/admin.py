from django.contrib import admin
from .models import Product, Order,Cart
from .form import ProductForm



class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name','slug','price','qte_stock','description','image','user')
    




admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Cart)




