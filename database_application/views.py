from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from database_application.models import User

def index(request):
    template = loader.get_template("database_application/home.html")
    context = {}
    return HttpResponse(template.render(context, request))


def user_table(request):
    usertable = User.objects.all()
    template = loader.get_template("database_application/table.html")
    context={'usertable':usertable,}
    return HttpResponse(template.render(context, request))


def query(request):
    #query = request.POST[input]
    return user_table(request)