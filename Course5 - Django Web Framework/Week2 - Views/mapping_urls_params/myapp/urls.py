from django.urls import path
from . import views

urlpatterns = [
    path('dishes/<str:dish>', views.menuitems),
]