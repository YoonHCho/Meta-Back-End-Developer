# App level
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # Add remaining URL path config here
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_items, name="menu_item"),
]