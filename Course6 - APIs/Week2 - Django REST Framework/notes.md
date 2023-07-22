## Installing and Setting up DRF (Django REST Framework)

using `pipenv` is easier than using `pip` since `pip` you'll need to manage all the dependencies and keep track of those packages. However `pipenv` which works on top of pip, makes everything easier with a lot of work going on behind the scenes. Creates and manages the virtual environment. You don't have to manually configure so many things to make it work.

1. Go to your project directory and run `pipenv install django` and once done, run `pipenv shell` to activate the virtual environment and it'll be ready to work.
2. Create django project `django-admin startproject BookList .` and then app `python manage.py startapp BookListAPI`
3. Install the DRF `pip3 install djangorestframework` OR `pipenv install djangorestframework` Once installed, need to configure DRF. Open the `settings.py` in project directory and find `INSTALLED_APPS` and add `rest_framework` in the list and also add the app to the list, in this case `BookListAPI`
4. In the `views.py` app level, need to add following:

   ```
   from django.shortcuts import render
   from rest_framework.response import Response
   from rest_framework import status
   from rest_framework.decorators import api_view

   @api_view() --> 'GET' as default?
   **@api_view(['POST', 'GET']) --> add HTTP methods
   ^ You can specify which HTTP methods your function should support
   def books(request):
       return Response('List of the books', status=status.HTTP_200_OK)
   ```

5. In `urls.py`

   ```
   * app level
   from django.urls import path
   from . import views
   urlpatterns = [
       path('books', views.books)
   ]

   * proj level
   from django.contrib import admin
   from django.urls import path, include
   urlpatterns = [
       path('admin', admin.site.urls),
       path('api/', include(BookListAPI.urls)),
   ]
   ```

## Restaurant menu API with DRF

Create django project, install DRF with virtual environment using pipenv, also start app called `LittleLemonAPI`. Make sure to add the `rest_framework` and `LittleLemonAPI` in `INSTALLED_APPS`
In `models.py` create a `MenuItem` class

```
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
```

Create file `serializers.py`

```
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
```

Crete file `views.py`

```
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

```

^ to function correctly, ListCreateAPIView needs two items, a queryset that retrieves all the records using a model and serializer class to display and store the records properly.

```
* `urls.py` app level
from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view())
]


* urls.py project level, add path
path('api/', include('LittleLemonAPI.urls'))
```
