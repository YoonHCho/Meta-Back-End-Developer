# models.py
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

# serializers.py
from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal
from .model import Category # from relationship_serializers.py, then add line 24

# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     inventory = serializers.IntegerField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.StringRelatedField() # once class MenuItemSerializer added remove this line and add line 30
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItem
        # fields = ['id', 'title', 'price', 'inventory']
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id'] # to change the name inventory to stock, add line 27

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1) # to link, add line 28 and add in fields array in line 34


# views.py
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def menu_item(request):
    # return Response('List of books', status=status.HTTP_200_OK)
    if request.method == 'GET':
        items = MenuItem.objects.selecte_related('category').all()
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST': # to deserialize data
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        # serialized_item.validated_data # if you need to access data before calling the save method, you can use this
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


@api_view
def single_item(request, id):
    # item = MenuItem.objects.get(pk=id)
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)