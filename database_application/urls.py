from django.urls import path

from database_application.views import index, query, users, utensils


urlpatterns = [
    path('', index, name='index'),
    path('users', users, name='users'),
    path('utensils', utensils, name='utensils'),
]