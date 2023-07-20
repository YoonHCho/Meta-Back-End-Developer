from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books),
    # path('books/<int:pk>', views.books),
]