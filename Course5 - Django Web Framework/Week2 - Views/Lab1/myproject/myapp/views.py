from django.shorcuts import render

# Create your views here
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Welcome to Little Lemon! </h1>")

# Create urls.py in myapp