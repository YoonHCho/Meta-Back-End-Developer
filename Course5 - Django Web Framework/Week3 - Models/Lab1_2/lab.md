The lab exercise doesn't have the complete directories and files to run server. Only created what I needed/had to code to solve the lab.

## Goal

The learner will learn how to use the Foreign Key between two Models in Django.

## Objectives

- The learner will create a model called DrinksCategory

- The learner will create a second model called Drinks to pass the argument for the foreign key in model attributes before performing migrations.

1. Create `DrainksCategory` (attr: category_name) and `Drinks` (attr: drink and price) in `models.py`
2. Inside the class Drinks, create a third attr `category_id` as a foreign key
3. `admin.py` import models needed and register both models
4. Run command to make migrations and to perform migration
5. Check if both `myapp_drinks` and `myapp_drinkscategory` tables are generated, after `Open Database` on `db.sqlite3`
6. Run command to start the interactive Python shell `python manage.py shell`. Once inside the Django shell, import `DrinksCategory` model `from myapp.models import DrinksCategory` then create variable and instantiate it using keyword arguments to the model class `cat = DrinksCategory(category_name='coffee')` finally use the `save()` to save to the database `cat.save()`
7. Check `SQLITE EXPLORER` and locate table `myapp_drinkscategory` and right click and choose `show table` to see that the record is entered into the table.
8. Create a drink in the `Drinks` table that uses foreign key from `DrinksCategory`
9. Still in the Django shell, import the `DrinksCategory` and `Drinks` model. Create a variable `fk` to store the foreign key, and retrieve it using the `objects.get()` method.
   `fk = DrinksCategory.objects.get(pk=1)`
   Note: The objects.get() method retrieves the value from the DrinksCategory model.
10. Next, create another variable drink and instantiate it using keyword arguments to the model class:
    `drink = Drinks(drink='mocha', price=7, category_id=fk)`
    Finally, use the `save()` method to save to the database.
    `drink.save()`
