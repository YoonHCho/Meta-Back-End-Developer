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