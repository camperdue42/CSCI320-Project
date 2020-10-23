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


def users(request):
    return return_table(request, {})
    usertable = User.objects.all()
    users_string = ""
    for user in usertable:
        users_string + str(user.Name)
        users_string + str(user.UID)
        users_string + '\n'
    context = {'title':'Users','usertable':usertable }
    return return_table(request, context)
