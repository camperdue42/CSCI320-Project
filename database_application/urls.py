from django.urls import path

from database_application.views import index

urlpatterns = [
    path('', index, name='index')
]