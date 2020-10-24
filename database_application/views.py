from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.template import Context, loader

from database_application.models import User, Utensil
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
    context = {'title':'Users','table':usertable }
    return return_table(request, context)


def utensils(request):
    utensiltable = Utensil.objects.all()
    utensils_string = ""
    for utensil in utensiltable:
        utensils_string += utensil.UtensilName + '\n'
    return return_table(request, {'title':'Utensils', 'table':utensils_string})

