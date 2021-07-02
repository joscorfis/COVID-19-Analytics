from django.shortcuts import render
from graphene import ObjectType, String, Schema
from main import queries
import requests

# Create your views here.

def index(request):
    return render(request,'index.html')

def lista_mas_visualizados(request):
    tipoRepo = 'Repositorios COVID con más observadores/watchers'
    lista = queries.get_repositorios_coronavirus_mas_visualizados()
    ids = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    visualizaciones = lista[3]
    mylist = zip(ids,nombres,fechaCreacion,visualizaciones)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    return render(request,'lista.html', {'tipo':tipoRepo, 'lista':mylist2})

def show(request):
    return render(request,'show.html')
    

