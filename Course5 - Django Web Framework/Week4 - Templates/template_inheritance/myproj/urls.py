# This is the Project level
from django.contrib import admin
from django.urls import path, include

# Create your urls here
urlpatterns = [
    path('admin', include(admin.site.urls)),
    path('', include('myapp.urls')),
]