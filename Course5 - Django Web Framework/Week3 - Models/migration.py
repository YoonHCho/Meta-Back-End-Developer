from django.db import models

# Create your models here
class Menuitems(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=300)
    year = models.IntegerField()

'''
Before migrating, make sure the app is included in the INSTALLED_APPS in the settings.py at project level

run command to make a migration: python manage.py makemigrations -> this prepare the changes to be made to a model
this will create migrations for the app, look at the details after running the command
it will create?? database such as db.sqlite3

run command to apply the migration: python manage.py migrate -> executes SQL commands to make changes to a model

can explore the details of the migrations using showmigrations command
python manage.py showmigrations
the 'X' symbol represents the status of applying migrations after making them. This is after the command make migrations, but before the command migrate.

To apply migration to a specific app, place the app after the command
python manage.py makemigrations <appName>>
'''
