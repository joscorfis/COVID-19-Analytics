from django.shortcuts import render
from graphene import ObjectType, String, Schema
from main import queries
import requests

# Create your views here.

def index(request):
    lista = queries.get_repositories_coronavirus
    return render(request,'index.html', {'lista':lista})

    

