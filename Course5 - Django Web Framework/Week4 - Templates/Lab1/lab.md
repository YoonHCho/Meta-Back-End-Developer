The lab exercise doesn't have the complete directories and files to run server. Only created what I needed/had to code to solve the lab.

## Goal

The learner will practice using Templates in Django

## Objectives

- The learner will create views for Menu and About page

- The learner will create respective templates for the two views

- The learner will pass the dictionary and other static content such as images inside the webpages created

1. In `settings.py` add `templates` in the `DIRS` option.
2. In `views.py` create functions for `about` and `menu`. Inside `about` function, create a variable `about-content` and assign a dictionary and code return accordingly with the new dictionary.
3. Create a folder called `templates` at the root project-level directory and create htmls for `about` and `menu`
4. Now we will work with static files, in `settings.py`, add `STATICFILES_DIRS` and add the values `'myapp/static',` to it. the file `static` is inside the `mypp` folder.
5. Place `{% load static %}` at the top of the file below `<!DOCTYPE html>` so that it loads the static before loading the doctype. and add `<img src="{% static 'img/dessert.jpg' %}" alt="">` at the location you want to render the image.
6. Make sure the `urls.py` is set in the app level and run the server to check if both path is working correctly.
