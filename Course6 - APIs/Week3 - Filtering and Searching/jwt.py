# activate VE, pipenv shell. pipenv install djangorestframework-simplejwt~=5.2.1

# settings.py
INSTALLED_APPS = [
    # add jwt
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist', # after this you should perform migration
]

REST_FRAMEWORK = {
    # add
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_frameowrk_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5)
}

# urls.py proj level
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatters = [
    # add
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenObtainPairView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]