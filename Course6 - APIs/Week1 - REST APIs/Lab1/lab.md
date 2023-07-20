Only included codes added to the online lab

## Goal

Your goal for this exercise is to create your project using plain Django and implement the features discussed in the video, Book list API project.

## Objectives

- Practice creating a Django model for a database table

- Create a function-based view

- Run the server to display the output of your APIs

- Use GET and POST methods to update a database table built from the model

Activate virtual environment using pipenv
`pipenv shell`
`pipenv install`

1. `models.py` app level, create class called `Book` and add attributes for `title`, `author`, `price` and create a `Meta` class inside the `Book` class with variable `indexes` and value `models.Index(fields=['price']),`
2. `admin.py` -> import the model and register.
3. Run command to perform migrations and run server and login as admin.
4. Select `Book` and add two books:
   - Title: Northanger Abbey - Author: Jane Austen - Price: 18.20
   - Title: Siddhartha - Author: Hermann Hesse - Price: 6.50
5. Create `urls.py` in app level (BookListAPI) and add a path for string `books` and view function `books`
6. Create `urls.py` in project level (BookList) and add path `api`
7. `views.py` app level and import the following:
   - The IntegrityError exception from the package django.db
   - JsonResponse function from the package django.http
   - The Book model from the models.py file present inside the same directory
   - The csrf_exempt decorator function from the package django.views.decorators.csrf
   - The model_to_dict function from the package django.forms.model
8. add the decorator `csrf_exempt` with `@` suffix, then define a view function `books` and implement code for the function.
