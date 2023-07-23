from django.shortcuts import render

# Create your views here
from .models import MenuItem
from .serializers import MenuItemsSerializer
from rest_framework import generics

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemsSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemsSerializer

