from django.urls import path
from . import views

# Create your urls here
urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
]