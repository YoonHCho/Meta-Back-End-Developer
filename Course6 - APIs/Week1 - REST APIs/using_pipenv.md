- Set up a new Django project in a virtual environment using pipenv.
- Use the virtual environment from the integrated terminal in VS Code.

1. First create a directory called LittleLemon `mkdir LittleLemon` and `cd` into the directory
2. `pipenv install django`
3. `pipenv shell` this will open a new shell session in the virtual environment for your project. Then use django admin to create a new django project in this directory. `django-admin startproject Littlelemon .`
4. `python manage.py startapp LittlelemonAPI` to create app for API
5. `python manage.py runserver`

Download and try Insomnia, GET & POST using https://httpbin.org/
