from django.urls import path
from . import views

urlpatterns = [
    path('ratings', views.RatingsView.as_view()),
]