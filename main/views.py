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
    observadores = lista[3]
    porcentajes = lista[4]
    mylist = zip(ids,nombres,fechaCreacion,observadores,porcentajes)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    mylist2_names = list(zip(*mylist2))[1]
    mylist2_watchers = list(zip(*mylist2))[3]
    return render(request,'lista_watchers.html', {'lista':mylist2, 'nombres':mylist2_names, 'watchers':mylist2_watchers})

def lista_mas_forks(request):
    lista = queries.get_repositorios_coronavirus_mas_forks()
    ids = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    forks = lista[3]
    porcentajes = lista[4]
    mylist = zip(ids,nombres,fechaCreacion,forks,porcentajes)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    mylist2_names = list(zip(*mylist2))[1]
    mylist2_forks = list(zip(*mylist2))[3]
    return render(request,'lista_forks.html', {'lista':mylist2, 'nombres':mylist2_names, 'forks':mylist2_forks})

def lista_mas_estrellas(request):
    lista = queries.get_repositorios_coronavirus_mas_estrellas()
    ids = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    estrellas = lista[3]
    porcentajes = lista[4]
    mylist = zip(ids,nombres,fechaCreacion,estrellas,porcentajes)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    mylist2_names = list(zip(*mylist2))[1]
    mylist2_stars = list(zip(*mylist2))[3]
    return render(request,'lista_stars.html', {'lista':mylist2, 'nombres':mylist2_names, 'estrellas':mylist2_stars})

def show(request):
    return render(request,'show.html')
    

