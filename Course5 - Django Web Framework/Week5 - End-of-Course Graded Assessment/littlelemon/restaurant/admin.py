from django.contrib import admin

# Register your models here.
from .models import Booking, Menu

admin.site.register(Booking)
admin.site.register(Menu)

# Run commands to make and perform migrations