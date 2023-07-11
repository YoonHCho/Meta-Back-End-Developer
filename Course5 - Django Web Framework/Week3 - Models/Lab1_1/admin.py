# app level admin.py
from django.contrib import admin

# Register your models here.
from .models import Drinks

admin.site.register(Drinks)
