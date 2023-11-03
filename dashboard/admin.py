from django.contrib import admin
from .models import Product, Grocery
from django.contrib.auth.models import Group

admin.site.site_header = 'TaoPo SuperUser Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']

class GroceryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Grocery, GroceryAdmin)
#admin.site.unregister(Group)