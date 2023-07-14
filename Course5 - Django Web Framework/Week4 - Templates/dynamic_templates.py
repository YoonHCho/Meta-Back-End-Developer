# views.py
from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    newMenu = {
        'mains': [
            {'name': 'falafel', 'price': '12'},
            {'name': 'shawarma', 'price': '15'},
            {'name': 'gyro', 'price': '10'},
        ]
    }
    return render(request, 'menu.html', newMenu)

'''
/templates/menu.html
<table>
  {% for item in mains %}
  <tr>
    <td>{{ item.name }}</td>
    <td>{{ item.price }}</td>
  </tr>
  {% endfor %}
</table>
'''


# MAPPING MODEL OBJECTS TO A TEMPLATE
# Create a dynamic menu by passing a model object to a template from a view
# models.py
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name

# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

def menu_by_id(request):
    newMenu = Menu.objects.all()
    newmenu_dict = {'menu': newMenu}
    return render(request, 'menu_cards.html', newmenu_dict)

# urls.py app level
from django.urls import path
from . import views

urlpatterns = [
    path('menu_card/', views.menu_by_id)
]

'''
templates/menu_cards.html

{{ menu }} # but this will render the QuerySet Object.

{% if menu %}
{% for item in menu %}
{{ item.name }} : {{ item.price }}
{% endfor %}
{% else %}
No item to Display
{% endif %}
'''