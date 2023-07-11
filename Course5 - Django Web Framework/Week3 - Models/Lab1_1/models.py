# app level models.py
from django.db import models

# Create your models here.
class Drinks(models.Model):
    # drink = models.CharField(max_length=200)
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()

'''
to make migration
python manage.py makemigrations

to apply migration
python manage.py migrate

to see the details
python manage.py showmigrations
'''