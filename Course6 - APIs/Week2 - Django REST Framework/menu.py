'''
Create django project, install DRF with virtual environment using pipenv, also start app called `LittleLemonAPI`. Make sure to add the `rest_framework` and `LittleLemonAPI` in `INSTALLED_APPS`
In `models.py` create a `MenuItem` class
'''
# models.py
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()


# Create file `serializers.py`
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']


# Crete file `views.py`
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
# ^ to function correctly, ListCreateAPIView needs two items, a queryset that retrieves all the records using a model and serializer class to display and store the records properly.

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# `urls.py` app level
from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view())
]


# urls.py project level, add path
path('api/', include('LittleLemonAPI.urls'))