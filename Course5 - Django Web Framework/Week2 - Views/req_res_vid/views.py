# views.py (app)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def home(request):
    path = request.path
    response = HttpResponse('This works!')
    # return HttpResponse(path, content_type='text/html', charset='utf-8')
    return response