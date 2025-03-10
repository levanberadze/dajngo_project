from django.shortcuts import render
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer
from rest_framework import viewsets


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(category_id=self.kwargs['category_id'])

