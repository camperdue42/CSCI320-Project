from django.urls import path

from database_application.views import index, user_table


urlpatterns = [
    path('', index, name='index'),
    path('users/', user_table, name='user_table'),
]