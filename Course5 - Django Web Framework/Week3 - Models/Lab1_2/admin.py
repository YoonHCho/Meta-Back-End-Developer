# app level
from django.contrib import admin
# Import the models from models.py
from .models import DrinksCategory
from .models import Drinks

# Register your models here.
admin.site.register(DrinksCategory)
admin.site.register(Drinks)

'''
Run following to make and perform migration
python manage.py makemigrations
python manage.py migrate
'''