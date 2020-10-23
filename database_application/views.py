from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader

from database_application.models import User, Utensil

#reference: https://docs.djangoproject.com/en/3.1/topics/db/queries/

def index(request):
    print("hello")
    context = {}
    return return_home(request, context)


def user_table(request):
    usertable = User.objects.all()
    users_string = ""
    for user in usertable:
        users_string + str(user.Name)
        users_string + str(user.UID)
        users_string + '\n'
    template = loader.get_template("database_application/table.html")
    context={'usertable':users_string,}
    return HttpResponse(template.render(context, request))


def return_home(request, context):
    """Renders the home page and returns it with a given context, doesn't really do anything on it's own but
    prevents having to redo everything every time"""
    template = loader.get_template("database_application/home.html")
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


def query(request):
    """Processes the user's query, figures out various different things, adding to database,
    modifying database, and displaying users information. Tasks generally delegated out to different
    functions"""
    query = request.POST.get('input', None)
    context = {}
    if query == None:
        return redirect('/database/')
    query_as_array = query.split(' ')
    if query_as_array[0].casefold() == "users".casefold():
        return user_table(request)

    elif query_as_array[0].casefold() == "Help".casefold():
        context = {'extra_stuff':'insert help text here'}
        return redirect('/database/')

    elif query_as_array[0].casefold() == "Add".casefold():
        context = {'extra_stuff':'Adding to database...'}
        add_to_database(query_as_array)
        return redirect('/database/')

    else:
        context = {'extra_stuff':'Invalid Command!'}
        return redirect(index)    


