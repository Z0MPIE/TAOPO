from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Chips/Snacks', 'Chips/Snacks'),
    ('Beverages', 'Beverages'),
    ('Instant Noodles', 'Instant Noodles'),
    ('Healthcare', 'Healthcare'),
    ('Pantry Items', 'Pantry Items'),
)

class Product(models.Model):
    
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveBigIntegerField(null=True)
    islow = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural= 'Inventory'

    def __str__(self):
        return f'{self.name}-{self.quantity}'
    

class Grocery(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveBigIntegerField(null=True)

    class Meta:
        verbose_name_plural= 'Grocery'

    def __str__(self):
        return f'{self.name}-{self.quantity}'