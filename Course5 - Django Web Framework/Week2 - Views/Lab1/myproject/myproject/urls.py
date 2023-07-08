from django.contrib import admin
from django.urls import path, include

# Create your urls here, add include function from the package django.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    # Update the urlpatterns here
    path('', include("myapp.urls")),
]

# the argument in include function, Django will look for URL patterns in "myapp.urls" to determine how to handle the request
# open the setting.py file and register the app by adding the myapp to the option INSTALLED_APPS, add the string "myapp.apps.MyappConfig"

'''
OR, instead of adding include function can also do below
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]


'''