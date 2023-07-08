# Create your urls here
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
]

# Go to the urls.py in the myproject folder.

'''
the urlpatterns will hold the URL patterns for Django project, is a list variable
first argument: '' -> this is the URL pattern or path you want to match. this case represents the root URL or the homepage of the Django application
second argument: views.home -> this argument specifies the view function associated with the URL pattern. refers to a function named home defined in the views.py file.
third argument: name="home" ->  (optional) This argument assigns a name to the URL pattern, which allows you to refer to it in your code using a unique identifier.
'''