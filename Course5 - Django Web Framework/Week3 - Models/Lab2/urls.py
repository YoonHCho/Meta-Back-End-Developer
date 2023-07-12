from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.form_view),
]