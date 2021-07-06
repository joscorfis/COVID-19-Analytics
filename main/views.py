from django.shortcuts import render
from graphene import ObjectType, String, Schema
from main import queries
from datetime import date
import dateutil.parser
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

def lista_mejores_lenguajes(request):
    lenguajes = queries.get_lenguajes_mas_utilizados()
    set_lenguajes = set(lenguajes)
    cuentas = []

    for i in set_lenguajes:
        cuentas.append(lenguajes.count(i))
    mylist = zip(set_lenguajes,cuentas)
    mylist2 = sorted(mylist, key=lambda x: x[1], reverse=True)
    lenguajes_ordenados = list(zip(*mylist2))[0]
    valores_ordenados = list(zip(*mylist2))[1]

    return render(request,'lista_languages.html', {'lista':mylist2, 'lenguajes':lenguajes_ordenados, 'valores':valores_ordenados})

def lista_primeros_repositorios(request):
    lista = queries.get_primeros_repositorios_coronavirus_creados()
    ids = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    tiempo = lista[3]
    set_tiempo = set(tiempo)
    cuentas = []

    for i in set_tiempo:
        cuentas.append(tiempo.count(i))
    mylist = zip(ids,nombres,fechaCreacion,tiempo)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    mygraph = zip(set_tiempo,cuentas)
    mygraph2 = sorted(mygraph, key=lambda x: x[0], reverse=True)
    mygraph2_tiempos = list(zip(*mygraph2))[0]
    mygraph2_valores = list(zip(*mygraph2))[1]

    return render(request,'lista_firsts_repos.html', {'lista':mylist2, 'tiempos':mygraph2_tiempos, 'valores':mygraph2_valores})    


def lista_mas_actualizados(request):
    lista = queries.get_repositorios_coronavirus_mas_actualizados()
    ids = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    ultimaModificacion = lista[3]
    tiempoModificacion = lista[4]
    ultimoCommit = lista[5]
    tiempoCommit = lista[6]
    grafica = lista[7]

    mylistUpdate = zip(ids,nombres,fechaCreacion,ultimaModificacion,tiempoModificacion)
    mylistUpdate2 = sorted(mylistUpdate, key=lambda x: x[4])
    
    mylistCommit = zip(ids,nombres,fechaCreacion,ultimoCommit,tiempoCommit)
    mylistCommit2 = sorted(mylistCommit, key=lambda x: x[4])

    grafica = sorted(grafica, reverse=True)
    grafica_rangos = list(zip(*grafica))[0]
    grafica_valoresM = list(zip(*grafica))[1]
    grafica_valoresC = list(zip(*grafica))[2]

    return render(request,'lista_updates.html', {'listaU':mylistUpdate2, 'listaC':mylistCommit2, 'rangos':grafica_rangos, 'valoresM':grafica_valoresM, 'valoresC':grafica_valoresC})


def show(request):
    return render(request,'show.html')
    

