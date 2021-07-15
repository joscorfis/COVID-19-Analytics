from django.shortcuts import render
from main import queries
from datetime import datetime
from dateutil.tz import UTC

# Create your views here.

def index(request):
    pandemia = queries.get_cifras_pandemia()
    return render(request,'index.html', {'contador':pandemia})

def lista_mas_visualizados(request):
    lista = queries.get_repositorios_coronavirus_mas_seguidores()
    propietarios = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    seguidores = lista[3]
    porcentajes = lista[4]
    pandemia = queries.get_cifras_pandemia()

    mylist = zip(propietarios,nombres,fechaCreacion,seguidores,porcentajes)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    mylist2_names = list(zip(*mylist2))[1]
    mylist2_watchers = list(zip(*mylist2))[3]

    return render(request,'lista_watchers.html', {'lista':mylist2, 'nombres':mylist2_names, 'watchers':mylist2_watchers, 'contador':pandemia})

def lista_mas_forks(request):
    lista = queries.get_repositorios_coronavirus_mas_forks()
    propietarios = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    forks = lista[3]
    porcentajes = lista[4]
    pandemia = queries.get_cifras_pandemia()

    mylist = zip(propietarios,nombres,fechaCreacion,forks,porcentajes)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    mylist2_names = list(zip(*mylist2))[1]
    mylist2_forks = list(zip(*mylist2))[3]

    return render(request,'lista_forks.html', {'lista':mylist2, 'nombres':mylist2_names, 'forks':mylist2_forks, 'contador':pandemia})

def lista_mas_estrellas(request):
    lista = queries.get_repositorios_coronavirus_mas_estrellas()
    propietarios = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    estrellas = lista[3]
    porcentajes = lista[4]
    pandemia = queries.get_cifras_pandemia()

    mylist = zip(propietarios,nombres,fechaCreacion,estrellas,porcentajes)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    mylist2_names = list(zip(*mylist2))[1]
    mylist2_stars = list(zip(*mylist2))[3]

    return render(request,'lista_stars.html', {'lista':mylist2, 'nombres':mylist2_names, 'estrellas':mylist2_stars, 'contador':pandemia})

def lista_mejores_lenguajes(request):
    lenguajes = queries.get_lenguajes_mas_utilizados()
    set_lenguajes = set(lenguajes)
    cuentas = []
    pandemia = queries.get_cifras_pandemia()

    for i in set_lenguajes:
        cuentas.append(lenguajes.count(i))
    mylist = zip(set_lenguajes,cuentas)
    mylist2 = sorted(mylist, key=lambda x: x[1], reverse=True)
    lenguajes_ordenados = list(zip(*mylist2))[0]
    valores_ordenados = list(zip(*mylist2))[1]

    return render(request,'lista_languages.html', {'lista':mylist2, 'lenguajes':lenguajes_ordenados, 'valores':valores_ordenados, 'contador':pandemia})

def lista_primeros_repositorios(request):
    lista = queries.get_primeros_repositorios_coronavirus_creados()
    propietarios = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    tiempo = lista[3]
    set_tiempo = set(tiempo)
    cuentas = []
    pandemia = queries.get_cifras_pandemia()

    for i in set_tiempo:
        cuentas.append(tiempo.count(i))
    mylist = zip(propietarios,nombres,fechaCreacion,tiempo)
    mylist2 = sorted(mylist, key=lambda x: x[3], reverse=True)
    mygraph = zip(set_tiempo,cuentas)
    mygraph2 = sorted(mygraph, key=lambda x: x[0], reverse=True)
    mygraph2_tiempos = list(zip(*mygraph2))[0]
    mygraph2_valores = list(zip(*mygraph2))[1]

    return render(request,'lista_firsts_repos.html', {'lista':mylist2, 'tiempos':mygraph2_tiempos, 'valores':mygraph2_valores, 'contador':pandemia})    


def lista_mas_actualizados(request):
    lista = queries.get_repositorios_coronavirus_mas_actualizados()
    propietarios = lista[0]
    nombres = lista[1]
    fechaCreacion = lista[2]
    ultimaModificacion = lista[3]
    tiempoModificacion = lista[4]
    ultimoCommit = lista[5]
    tiempoCommit = lista[6]
    grafica = lista[7]
    pandemia = queries.get_cifras_pandemia()

    mylistUpdate = zip(propietarios,nombres,fechaCreacion,ultimaModificacion,tiempoModificacion)
    mylistUpdate2 = sorted(mylistUpdate, key=lambda x: x[4])
    
    mylistCommit = zip(propietarios,nombres,fechaCreacion,ultimoCommit,tiempoCommit)
    mylistCommit2 = sorted(mylistCommit, key=lambda x: x[4])

    grafica = sorted(grafica, reverse=True)
    grafica_rangos = list(zip(*grafica))[0]
    grafica_valoresM = list(zip(*grafica))[1]
    grafica_valoresC = list(zip(*grafica))[2]

    return render(request,'lista_updates.html', {'listaU':mylistUpdate2, 'listaC':mylistCommit2, 'rangos':grafica_rangos, 'valoresM':grafica_valoresM, 'valoresC':grafica_valoresC, 'contador':pandemia})

def grafica_de_evolucion(request):
    lista = queries.get_evolucion_repositorios_coronavirus([],"2019-12-30")
    nombres = lista[0]
    fechaCreacion = lista[1]
    ids = lista[2]
    ids_github = lista[3]
    grafica = lista[4]
    pandemia = queries.get_cifras_pandemia()

    mylist = zip(nombres,fechaCreacion,ids,ids_github)
    mylist2 = sorted(mylist, key=lambda x: x[2])

    grafica_rangos = grafica[1]
    grafica_valores = grafica[2]

    return render(request,'evolution_graph.html', {'lista':mylist2, 'rangos':grafica_rangos, 'valores':grafica_valores, 'contador':pandemia})

def lista_mas_proyectos(request):
    lista = queries.get_repositorios_coronavirus_mas_proyectos([],"2019-12-31T00:00:00+00:00")
    nombres = lista[0]
    propietario = lista[1]
    fechaCreacion = lista[2]
    proyectos = lista[3]
    pandemia = queries.get_cifras_pandemia()

    mylist = zip(nombres,propietario,fechaCreacion,proyectos)
    mylist2 = sorted(mylist, key=lambda x: len(x[3]), reverse=True)

    return render(request,'lista_projects.html', {'lista':mylist2, 'contador':pandemia})


def show(request,name_owner):
    nom_y_prop = name_owner.split("·")
    nombre = nom_y_prop[0]
    propietario = nom_y_prop[1]
    lista = queries.get_information_from_repository(nombre, propietario)
    pandemia = queries.get_cifras_pandemia()

    return render(request,'show.html', {'lista': lista, 'contador':pandemia})
    

def lista_mejores_paises(request):
    paises = queries.get_paises_mas_repositorios()
    set_paises = set(paises)
    cuentas = []
    pandemia = queries.get_cifras_pandemia()

    for i in set_paises:
        cuentas.append(paises.count(i))
        
    mylist = zip(set_paises,cuentas)
    mylist2 = sorted(mylist, key=lambda x: x[1], reverse=True)
    paises_ordenados = list(zip(*mylist2))[0]
    valores_ordenados = list(zip(*mylist2))[1]

    return render(request,'lista_countries.html', {'lista':mylist2, 'paises':paises_ordenados, 'valores':valores_ordenados, 'contador':pandemia})
