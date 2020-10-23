from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from database_application.models import User

def index(request):
    context = {}
    return return_home(request, context)


def user_table(request):
    usertable = User.objects.all()
    template = loader.get_template("database_application/table.html")
    context={'usertable':usertable,}
    return HttpResponse(template.render(context, request))


def return_home(request, context):
    template = loader.get_template("database_application/home.html")
    return HttpResponse(template.render(context, request))


def add_to_database(array):
    if array[1].casefold() == "Utensil".casefold():
        Utensil.objects.create(UtensilName = " ".join(array[2:]))


def query(request):
    query = request.POST.get('input', ' ')
    query_as_array = query.split(' ')
    if query_as_array[0] == "users":
        return user_table(request)
    elif query_as_array[0].casefold() == "Help".casefold():
        context = {'extra_stuff':'insert help text here'}
        return return_home(request, context)
    elif query_as_array[0].casefold() == "Add".casefold():
        context = {'extra_stuff':' '}
        return return_home(request, context)
    else:
        context = {'extra_stuff':'Invalid Command!'}
        return return_home(request, context)    
