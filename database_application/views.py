from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.template import Context, loader

from database_application.models import User, Utensil, Recipe, Ingredient, Step
from database_application.views_helper import *

#reference: https://docs.djangoproject.com/en/3.1/topics/db/queries/

def index(request):
    context = {}
    if request.method == "GET":
        return return_home(request, context)
    elif request.method == "POST":
        return query(request)


def users(request): #this is a bigtime todo but i cba right now
    usertable = User.objects.all()
    users_string = ""
    for user in usertable:
        users_string += str(user.UID) + " " + user.Name + "\n" 
    return return_table(request, {'title':"Users", 'table':users_string})


def utensils(request):
    utensiltable = Utensil.objects.all()
    utensils_string = ""
    for utensil in utensiltable:
        utensils_string += utensil.UtensilName + '\n'
    return return_table(request, {'title':'Utensils', 'table':utensils_string})


def recipe(request):
    recipetable = Recipe.objects.all()
    recipes_string = ""
    recipes_string = "Recipe Name  Prep Time  Price\n"
    for recipe in recipetable:
        recipes_string += recipe.RecipeName + " " + str(recipe.PreparationTime) + " " + str(recipe.Price) + "\n"
    return return_table(request, {'title':"Recipes", 'table':recipes_string})


def ingredients(request):
    ingredienttable = Ingredient.objects.all()
    ingredients_string = ""
    for ingredient in ingredienttable:
        ingredients_string += ingredient.IngredientName + " " + str(ingredient.AmountLeft) + "\n"
    return return_table(request, {'title':"Ingredients", 'table':ingredients_string})


def steps(request):
    steptable = Step.objects.all()
    step_string = ""
    for step in steptable:
        ingredients = ""
        for ingredient in step.Ingredients.all():
            ingredients += str(ingredient) + ",Ks "
        step_string += str(step.RecipeName) + " step " + str(step.StepNumber) + ": " + ingredients + "\n" + step.Instructions + "\n" + "\n"
    return return_table(request, {'title':'Steps', 'table':step_string})