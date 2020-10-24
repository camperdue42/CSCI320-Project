from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader

from database_application.models import User, Utensil

def query(request):
    """Processes the user's query, figures out various different things, adding to database,
    modifying database, and displaying users information. Tasks generally delegated out to different
    functions"""
    query = request.POST.get('input')
    query_as_array = query.split()
    if query_as_array[0].casefold() == "users".casefold():
        return redirect('/database/users')
    elif query_as_array[0].casefold() == "Utensils".casefold():
        return redirect('/database/utensils')
    elif query_as_array[0].casefold() == "Recipes".casefold():
        return redirect('/database/recipe')
    elif query_as_array[0].casefold() == "Ingredients".casefold():
        return redirect('/database/ingredients')
    elif query_as_array[0].casefold() == "Help".casefold():
        context = {'extra_stuff':'insert help text here'}
        return return_home(request, context)
    elif query_as_array[0].casefold() == "Add".casefold():
        context = {'extra_stuff':'Adding to database...'}
        add_to_database(query_as_array)
        return return_home(request, context)
    else:
        context = {'extra_stuff':'Invalid Command!'}
        return return_home(request, context)


def return_home(request, context):
    """Renders the home page and returns it with a given context, doesn't really do anything on it's own but
    prevents having to redo everything every time"""
    #template = loader.get_template("database_application/home.html")
    return render(request, 'database_application/home.html', context)


def return_result(request, context):
    template = loader.get_template("database_application/query_result.html")
    return HttpResponse(template.render(context, request))


def add_to_database(array):
    """Function used for creation of new models and adding them to the database, mainly a
    helper function for the query command altough I guess it could technically be used elsewhere"""
    if array[1].casefold() == "Utensil".casefold():
        utensil = Utensil(name=array[2:])
        utensil.save()
    
    if array[1].casefold() == "User".casefold():
        user = User(name=array[2:])
        user.save()


def return_table(request, context):
    return render(request, 'database_application/table.html', context)

