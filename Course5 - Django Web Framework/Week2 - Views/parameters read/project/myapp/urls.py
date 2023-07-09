from django.urls import path
from . import views

urlpatterns = [
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"),
    path("getform/", views.getform, name='getform'),
    path('', views.home, name='home'),
]