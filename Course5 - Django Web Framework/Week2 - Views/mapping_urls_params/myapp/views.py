from django.shortcuts import render
from django.http import HttpResponse

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from...',
        'falafel': 'Falafel are deep fried patties...',
        'cheesecake': 'Cheesecake is a type of dessert...'
    }
    description = items[dish]
    return HttpResponse(f'<h2>{dish}</h2> <p>{description}</p>')