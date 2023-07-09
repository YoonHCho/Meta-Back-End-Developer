from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def drinks(request, drink_name):
    drinks = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drinks[drink_name]
    return HttpResponse(f'<h2>{drink_name}</h2><p>{choice_of_drink}</p>')