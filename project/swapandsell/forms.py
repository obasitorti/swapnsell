from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'condition',
            'sale_type',
            'product_type',
            'price',
            'address',
            'photo_of_product',
            'another_photo',
            'contact_number'
        ]