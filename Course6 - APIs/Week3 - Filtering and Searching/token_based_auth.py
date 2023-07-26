'''
settings.py inside the INSTALLED_APPS add 'rest_framework.authtoken'
make sure your virtual environment is active 'pipenv shell'
create admin to access the django admin panel 'python manage.py createsuperuser'
click add for Tokens, and add token by selecting user: this case admin, once you click save, you will see the token key
'''

# in views.py to create protected API endpoint, continuation from the folder notes-folder from this week. add following, should be line 63 from views.py
# importing all the stuff again
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status
from decimal import Decimal
from django.core.paginator import Paginator, EmptyPage

# to create protected API endpoint
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# line 63
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "Some secret message"})

# after creating manager group, but needs to also check if currently authenticated user belongs to the manager group - User Role
@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({'message': 'Only Manager Should See This'})
    else:
        return Response({'message': 'You are not authorized'}, 403)


# for throttling
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle

@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({'message': 'Successful'})

# only for authenticated users
@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_auth(request):
    return Response({'message': 'Message for the logged in users only'})

# anther API endpoint with different limits
from .throttles import TenCallsPerMinute

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({'message': 'message for the logged in users only'})




# urls.py, add the path
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

path('secret/', views.secret),
path('api-token-auth/', obtain_auth_token),
path('manager-view/', views.manager_view),
path('throttle-check', views.throttle_check),
path('throttle-check-auth', views.throttle_check_auth),



# settings.py inside the REST_FRAMEWORK add
'''
'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    # ^ If you want to use the Django admin login simultaneously with a browsable API view of Djoser, you need to add this session authentication class too
),
'DEFAULT_THROTTLE_RATES': {
    'anon': '2/minute',
    'user': '5/minute'
} # 20/day, 1/second 20/hour etc
'''

# throttles.py to add another policy for other API endpoints
from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'
# ^ import this to the views.py

# settings.py inside 'DEFAULT_THROTTLE_RATE' add 'ten': '10/minute'

'''
Djoser - for better authentication.
Activate VE 'pipenv shell' then install Djoser 'pipenv install djoser' then open settings.py add 'djoser' inside INSTALLED_APPS.
Important to note that djoser is placed after the rest_framework. and a new field for DJOSER = {"USER_ID_FIELD": "username"}.
'''
# Djoser you need to enable it in urls.py project level for Djoser endpoint
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('LittleLemonAPI.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
