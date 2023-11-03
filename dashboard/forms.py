from django import forms
from .models import Product
from .models import Grocery

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity',]
    

class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = ['name', 'category', 'quantity',] 