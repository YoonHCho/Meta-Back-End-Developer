# models.py file in the app level
from unicodedata import name
from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " : " + self.cuisine

# (menuapp is the app name, models is the .py file) to access class Menu
# include menuapp in the settings.py, run the python shell, python manage.py shell, from menuapp.models import Menu
# python manage.py makemigrations, python manage.py migrate

'''
to create records
m = Menu.objects.create(namme = 'pasta', cuisine = 'italian', price = 10)
n = Menu.objects.create(namme = 'taco', cuisine = 'mexican', price = 2)

to show all the objects
Menu.objects.all()

to update entries
p = Menu.objects.get(pk=2)
p.cuisine = 'chinese'
p.save()
Menu.objects.all()
'''