from django.db import models
from core.models import BaseModel
import random
import string


class Item(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    stock_qty = models.PositiveIntegerField()
    height = models.PositiveIntegerField(null=True)
    width = models.PositiveIntegerField(null=True)
    weight = models.PositiveIntegerField(null=True)
    barcode = models.CharField(max_length=13, unique=True, editable=False)
    expiration_date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='items')

    def generate_barcode(self):
        return ''.join(random.choices(string.digits, k=13))

    def save(self, *args, **kwargs):
        self.barcode = self.generate_barcode()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



