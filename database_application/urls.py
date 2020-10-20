from django.urls import path

from database_application.views import index
from database_application.views import users

urlpatterns = [
    path('', index, name='index'),
    path('users/', users, name='users'),
]