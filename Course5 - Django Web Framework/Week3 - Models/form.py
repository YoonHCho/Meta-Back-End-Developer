from django import forms
from django.forms.widgets import NumberInput

FAVORITE_DISH = [
    ('italian', 'Italian'),
    ('greek', 'Greek'),
    ('turkish', 'Turkish'),
]

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100, required=False, initial='Enter your name')
    age = forms.IntegerField(help_text='A valid age is required')

class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    email = forms.EmailInput(label="Enter email address")
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    favorite_dish = forms.ChoiceField(choices=FAVORITE_DISH) # this is select
    favorite_dish = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_DISH) # radio


# Create Form in forms.py in app level
from django import forms

SHIFTS = (
    ('1', 'Morning'),
    ('2', 'Afternoon'),
    ('3', 'Evening'),
)

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField(help_text="Enter the exact time")

# in views.py app level
from django.shorcuts import render
from myapp.forms import InputForm

def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "home.html", context)

# then create a templates folder in myapp, and create home.html file. in home.html


# Model Form, models.py (this is an example of model form for lines from 22)
from django.db import models

# Create your models here
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time")

# can delete the InputForms class inside the forms.py and replace it with below
from django import forms
from .models import Logger

class LogForm(forms.ModelForms):
    class Meta:
        model = Logger
        fields = '__all__' # this will import all fields from Logger

# then register the model, go to admin.py
from django.contrib import admin
from .models import Logger
# Register your models here
admin.site.register(Logger)

# in views.py
from myapp.forms import LogForm

def form_view(request):
    form = InputForm()
    # update conditional statement below
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "home.html", context)