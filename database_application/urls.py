from django.urls import path

from database_application.views import index, query


urlpatterns = [
    path('', index, name='index'),
    path('query', query, name='query'),
]