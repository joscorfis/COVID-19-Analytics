from django.shortcuts import render
from graphene import ObjectType, String, Schema
from main import queries
import requests

# Create your views here.

def index(request):
    return render(request,'index.html')

def lista_mas_visualizados(request):
    lista = queries.get_repositorios_coronavirus_mas_visualizados()
    ids = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    visualizaciones = lista[3]
    porcentajes = lista[4]
    mylist = zip(ids,nombres,fechaCreacion,visualizaciones,porcentajes)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    return render(request,'lista_watchers.html', {'lista':mylist2})

def lista_mas_forks(request):
    lista = queries.get_repositorios_coronavirus_mas_forks()
    ids = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    forks = lista[3]
    porcentajes = lista[4]
    mylist = zip(ids,nombres,fechaCreacion,forks,porcentajes)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    return render(request,'lista_forks.html', {'lista':mylist2})

def show(request):
    return render(request,'show.html')
    

