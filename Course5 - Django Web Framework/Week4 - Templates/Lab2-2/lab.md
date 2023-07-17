The lab exercise doesn't have the complete directories and files to run server. Only created what I needed/had to code to solve the lab.

## Goal

The learner will practice using partial Templates in Django

## Objectives

- The learner will use partial templates using keywords include and extends

1. Open `settings.py` in myproject, and set the value of `STATICFILES_DIRS` option to `myproject/static`. In `views.py` create four functions, `home`, `menu`, `about`, `book` and code the render function.
2. Open `templates` and create a folder `partial` inside it. inside `partial`, create a file `_header.html`. Add code for the html files. Inside, make sure to add `{% load static %}` to get the image (dummy)
3. Open `.html` files and code accordingly so that it extends, loads, and renders content.
4. Run server and check if all runs accordingly.
