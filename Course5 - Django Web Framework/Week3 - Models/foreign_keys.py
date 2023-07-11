# models.py in app level
from django.db import models

# Create your models here, create 2 models
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    # foreign key requires two fields, 1st class for the model to connect to and 2nd is the settings field that, in this case, enables on_delete
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name='category_name')


# admin.py in app level
from django.contrib import admin
from .models import Menu
from .models import MenuCategory

# register your models here
admin.site.register(Menu)
admin.site.register(MenuCategory)

# make sure the INSTALLED_APPS in settings.py is updated