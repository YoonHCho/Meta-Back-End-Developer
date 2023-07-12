# to create a user for admin, run command python3 manage.py createsuperuser
# then follow the prompt to create a username, input an email address, and create password

# To unregister a user, in admin.py
from django.contrib import admin
from django.contrib.auth.models import User

admin.site.unregister(User)

# to register our own admin, use @admin.register() decorator. give the user a model as the argument. decorate a sub-class of UserAdmin class
from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]

# Create a user
from django.contrib.auth.models import User
usr = User.objects.create_user('username', 'email@email.com', 'password')
# Create a staff user
usr.is_staff = True
usr.save()

# Create a superuser
# python manage.py createsuperuser --username=john --email=john@email.com --password=password

'''
Adding groups and Users
1. Create a user
python manage.py createsuperuser
then follow prompt to create username, input email address, and create password
'''
# admin.py app level
from django.contrib import admin
from myapp.models import Reservation # class Reservation in models.py

admin.site.register(Reservation)

# log in as admin, and create reservations for MYAPP.
# models.py
from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    # below will help show the name of the reservation when viewing from the admin dashboard
    # __str__ method returns the string representation of the object
    def __str__(self):
        return self.name



### PERMISSIONS ###
'''
Enable permission settings
<app>.<action_model>
  |     |       |-> name of the model
  |     |-> Add, change, delete, or view
  |-> name of the Django App

assume that a django app called my app is created in the current project and it hasa a model with the name mymodel declared in it.
the permission on this model will be:
myapp.add_mymodel
myapp.change_mymodel
myapp.delete_mymodel
myapp.view_mymodel

'''