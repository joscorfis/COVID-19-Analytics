from django.shortcuts import render
from graphene import ObjectType, String, Schema
from main import queries
import requests

# Create your views here.

def index(request):
    return render(request,'index.html')

def lista(request):
    ids = queries.get_repositories_coronavirus()[0]
    nombres = queries.get_repositories_coronavirus()[1]
    creaciones = queries.get_repositories_coronavirus()[2]
    issues = queries.get_repositories_coronavirus()[3]
    print(ids)
    mylist = zip(ids,nombres,creaciones,issues)
    return render(request,'lista.html', {'lista':mylist})

def show(request):
    return render(request,'show.html')
    

