# view.py
from django.http import HttpResponse
def index(request, name):
    return HttpResponse("<h1>Hello, {}. </h1>".format(name))

# However using Python's string substitution (like above) is not efficient. That's why you use the templates

'''
create hello.html file and place it in the templates folder in the Django project's BASE_DIR
<html>
  <head>
    <title>My django website</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>

To render a Template, import the loader class from django.template module
'''

# views.py
from django.shorcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('hello.html')
    context = {}
    return HttpResponse(template.render(context, request))
    # OR
    # return render(request, 'hello.html', {})

'''
VARIABLE TAGS
In the above code, the render() function’s third parameter is an empty dictionary object. It is called the template context.
You should pass the path parameter as a context to hello.html
'''
from django.shortcuts import render

def index(request, name):
    context={"name":name}
    return render(request, 'hello.html', context)

'''
Modify the hello.html file by replacing World with the Django variable syntax.
Put the key of the context dictionary name inside double curly brackets as in {{ name }}.

<h1>Hello {{ name }}</h1>

You can use {% if %} tag of DTL to implement a conditional logic inside the template.
Similarly, with {% for%} and{% endfor %} tags, a looping construct can be built in the template, which may be useful to display records
from a database table on the web page. Django’s Template Language has many more tags.
'''

'''
FILTERS
Filters merely represent the temporarily modified value of a template variable, Syntax
{{ variable_name | filter_name }}

{{ name | upper }}
if the value of the variable name is 'john' it will render uppercase john -> 'JOHN'
'''

##### EXAMPLE #####
# views.py
from django.shorcuts import render

def about(request):
    about_content = {'about': 'This is about page of Little Lemon Restaurant'}
    return render(request, 'about.html', about_content)

# urls.py app level
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about")
]

# urls.py project level
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls'))
]

# settings.py proj level
TEMPLATES = [
    {
        # Add value to 'DIRS'
        'DIRS': ['templates']
    }
]
INSTALLED_APPS = [
    # Add myapp
    'myapp.apps.MyappConfig'
]

# about.html inside templates folder in the outer (main) project folder
'''
<h2>ABOUT</h2>
<p>{{ about }}</p>
'''