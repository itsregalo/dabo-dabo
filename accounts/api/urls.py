from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api-accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
urlpatterns = format_suffix_patterns(urlpatterns)