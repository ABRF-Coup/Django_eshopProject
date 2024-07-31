
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','qte_stock','description', 'image']


    def clean_slug(self):
        return self.cleaned_data.get('slug')
        