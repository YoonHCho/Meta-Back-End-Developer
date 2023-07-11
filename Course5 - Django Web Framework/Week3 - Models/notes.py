
'''
Example of Migration, when working with SQL, if wanted to add a column you would do following

** SQL Alter statement **
ALTER TABLE user
ADD COLUMN city VARCHAR(255) NOT NULL

however when working with models in Django, you can just add the attribute to the class.
'''
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # add the attribue to add a column in the table
    city = models.CharField(max_length=30)

# then run the migration scripts to implement the changes
# manage.py makemigrations
# manage.py migrate

