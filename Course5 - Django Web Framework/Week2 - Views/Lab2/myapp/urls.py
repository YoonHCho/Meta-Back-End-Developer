from django.urls import path
from . import views

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name='drinks'),
]