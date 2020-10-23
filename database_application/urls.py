from django.urls import path

from database_application.views import index, query, users


urlpatterns = [
    path('', index, name='index'),
    path('users', users, name='users')
]