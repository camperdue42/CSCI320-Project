from django.urls import path

from database_application.views import index, query, users, utensils, recipe, ingredients, steps


urlpatterns = [
    path('', index, name='index'),
    path('users', users, name='users'),
    path('utensils', utensils, name='utensils'),
    path('recipe', recipe, name='recipe'),
    path('ingredients', ingredients, name='ingredients'),
    path('steps', steps, name='steps')
]