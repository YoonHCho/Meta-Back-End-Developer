# Namespacing

# in the app's urls.py
from django.urls import path
from . import views

# USING Instance Namespace
urlpatterns = [
    path('namespace/', include('demoapp.urls', namespace='demoapp')),
]

# OR Application Namespace
app_name = 'demoapp'

urlpatterns = [
    # your normal path functions here.
]

# Using namespace in view
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

def myview(request):
    # some function
    return HttpResponsePermanentRedirect(reverse('demoapp:login'))

# Namespace in the URL tag
'''
<form action="/demoapp/login" method="POST">
  <input type='submit'>
</form>
'''

'''
The form will then be processed by the view mapped to this URL. However, as mentioned above, a hard-coded URL is not desired. Instead, use the url tag of the Django Template Language. It returns the absolute path from the named URL. 

Use the url tag to obtain the URL path dynamically, as shown below:
<form action="{% url 'login' %}" method="post">
  #form attributes
  <input type='submit'>
</form>

** the login view may be present in multiple apps. Use the named URL qualified with the namespace to resolve the conflict.
<form action="{% url 'demoapp:login' %}" method="post">
'''

# in Django application, a view function is where all the processing is done. it receives the request and formulates the response.
from django.http import HttpResponse, HttpResponseNotFound

def my_view(request):
    # code
    if condition == True:
        return HttpResponse('<h1>Page not found</h1>', status_code='404')
        # OR
        # return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')

'''
Consider the following scenario, where you have a Product model in the app.
The user wants the details of a product with a specific Product ID.
In the following view function, id is the parameter obtained from the URL.
It tries to determine whether any product with the given id is available. If not, the Http404 exception is raised.
'''
from django.http import Http404, HttpResponse
from .models import Product

def detail(request, id):
    try:
        p = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return HttpResponse("Product Found")

# To display the custom error message in the browser, change DEBUG = False in settings.py