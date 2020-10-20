from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from .models import user

def index(request):
    template = loader.get_template("database_application/home.html")
    context = {}
    return HttpResponse(template.render(context, request))

def users(request):
    usertable = user.objects.all()
    template = loader.get_template("database_application/table.html")
    context={}
    return HttpResponse(template.render(context, request))
