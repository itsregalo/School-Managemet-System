from django.urls import path
from accounts.api.views import RegistrationApiView

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api_accounts'

urlpatterns = [
    path('register/', RegistrationApiView, name='register-api'),
    path('login/', obtain_auth_token, name='login-api'),
]