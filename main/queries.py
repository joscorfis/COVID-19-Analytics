from dateutil.tz import UTC
from graphene import ObjectType, String, Schema
from datetime import date, datetime, timedelta, timezone
import dateutil.parser
import requests
import json
import pandas as pd
import numpy as np
from functools import partial
from geopy.geocoders import Nominatim

headers = {"Authorization": "token 7efc823e322b745df4ef31c4e95ff44327a029f3"}

#=================
# METODO PRINCIPAL
#=================

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.

    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

#==========
# CONSULTAS
#==========

def get_repositorios_coronavirus_mas_visualizados():

    query = """
    {
        search(query: "topic:covid-19  followers:>=20", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            name
            owner {
                login
            }
            createdAt
            watchers {
                totalCount
            }
            }
        }
        }
    }
    }
    """    

    result = run_query(query) # Execute the query
    num_results = int(result["data"]["search"]["repositoryCount"])
    if(num_results>100):
        num_results = 100
    propietarios = []
    nombres = []
    fechaCreacion = []
    observadores = []
    porcentajes = []
    for i in range(num_results):
        propietarios.append(result["data"]["search"]["edges"][i]["node"]["owner"]["login"])
        nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
        fechaCreacion.append(date_time_formatter(result["data"]["search"]["edges"][i]["node"]["createdAt"]))
        observadores.append(result["data"]["search"]["edges"][i]["node"]["watchers"]["totalCount"])
        if(i<1):
            max_observadores = observadores[0]
            porcentajes.append(100)
        else:
            porcentajes.append((result["data"]["search"]["edges"][i]["node"]["watchers"]["totalCount"]/max_observadores)*100)
    return [propietarios,nombres,fechaCreacion,observadores,porcentajes]  


def get_repositorios_coronavirus_mas_forks():

    query = """
    {
    search(query: "topic:covid-19 forks:>=60", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            name
            owner {
                login
            }
            createdAt
            forks {
                totalCount
            }
            }
        }
        }
    }
    }
    """    

    result = run_query(query) # Execute the query
    num_results = int(result["data"]["search"]["repositoryCount"])
    if(num_results>100):
        num_results = 100
    propietarios = []
    nombres = [] 
    fechaCreacion = []
    forks = [] 
    porcentajes = []
    for i in range(num_results):
        propietarios.append(result["data"]["search"]["edges"][i]["node"]["owner"]["login"])
        nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
        fechaCreacion.append(date_time_formatter(result["data"]["search"]["edges"][i]["node"]["createdAt"]))
        forks.append(result["data"]["search"]["edges"][i]["node"]["forks"]["totalCount"])
        if(i<1):
            max_forks = forks[0]
            porcentajes.append(100)
        else:
            porcentajes.append((result["data"]["search"]["edges"][i]["node"]["forks"]["totalCount"]/max_forks)*100)

    return [propietarios,nombres,fechaCreacion,forks,porcentajes]  


def get_repositorios_coronavirus_mas_estrellas():

    query = """
    {
    search(query: "topic:covid-19 stars:>=160", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            name
            owner {
                login
            }
            createdAt
            stargazers {
                totalCount
            }
            }
        }
        }
    }
    }
    """    

    result = run_query(query) # Execute the query
    num_results = int(result["data"]["search"]["repositoryCount"])
    if(num_results>100):
        num_results = 100
    propietarios = []
    nombres = [] 
    fechaCreacion = []
    estrellas = [] 
    porcentajes = []
    for i in range(num_results):
        propietarios.append(result["data"]["search"]["edges"][i]["node"]["owner"]["login"])
        nombres.append(str(result["data"]["search"]["edges"][i]["node"]["name"]))
        fechaCreacion.append(date_time_formatter(result["data"]["search"]["edges"][i]["node"]["createdAt"]))
        estrellas.append(result["data"]["search"]["edges"][i]["node"]["stargazers"]["totalCount"])
        if(i<1):
            max_stars = estrellas[0]
            porcentajes.append(100)
        else:
            porcentajes.append((result["data"]["search"]["edges"][i]["node"]["stargazers"]["totalCount"]/max_stars)*100)

    return [propietarios,nombres,fechaCreacion,estrellas,porcentajes] 


def get_lenguajes_mas_utilizados():

    query = """
    {
    search(query: "topic:covid-19 stars:>100", type: REPOSITORY, first: 100) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            stargazers {
                totalCount
            }
            languages(first: 10) {
                totalCount
                nodes {
                name
                }
            }
            }
        }
        }
    }
    }
    """    

    result = run_query(query) # Execute the query
    num_results = int(result["data"]["search"]["repositoryCount"])
    if(num_results>100):
        num_results = 100
    lenguajes = []
    for i in range(num_results):
        num_language_res = int(result["data"]["search"]["edges"][i]["node"]["languages"]["totalCount"])
        if(num_language_res>10):
            num_language_res = 10
        for j in range(num_language_res):
            lenguajes.append(result["data"]["search"]["edges"][i]["node"]["languages"]["nodes"][j]["name"])
    
    return lenguajes   


def get_primeros_repositorios_coronavirus_creados():

    query = """
    {
    search(query: "topic:covid-19 sort:updated-asc stars:>1", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            name
            owner {
                login
            }
            createdAt
            updatedAt
            }
        }
        }
    }
    }
    """    

    result = run_query(query) # Execute the query
    num_results = int(result["data"]["search"]["repositoryCount"])
    if(num_results>100):
        num_results = 100
    propietarios = []
    nombres = []
    fechaCreacion = []
    tiempo = []
    for i in range(num_results):
        createAt = result["data"]["search"]["edges"][i]["node"]["createdAt"]
        if dateutil.parser.isoparse(createAt).date() > date(2019,12,31):
            propietarios.append(result["data"]["search"]["edges"][i]["node"]["owner"]["login"])
            nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
            fechaCreacion.append(date_time_formatter(createAt))
            tiempo.append(days_until_now(createAt))

    return [propietarios,nombres,fechaCreacion,tiempo]  


def get_repositorios_coronavirus_mas_actualizados():

    query = """
    {
    search(query: "topic:covid-19 sort:updated-desc stars:>1", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            name
            owner {
                login
            }
            createdAt
            updatedAt
            defaultBranchRef{
                target{
                ... on Commit{
                    history(first:1){
                    edges{
                        node{
                        ... on Commit{
                            committedDate
                        }
                        }
                    }
                    }
                }
                }
            }
            }
        }
        }
    }
    }
    """    

    result = run_query(query) # Execute the query
    num_results = int(result["data"]["search"]["repositoryCount"])
    if(num_results>100):
        num_results = 100
    propietarios = []
    nombres = []
    fechaCreacion = []
    ultimaModificacion = []
    tiempoModificacion = []
    ultimoCommit = []
    tiempoCommit = []
 
    for i in range(num_results):
        propietarios.append(result["data"]["search"]["edges"][i]["node"]["owner"]["login"])
        nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
        fechaCreacion.append(date_time_formatter(result["data"]["search"]["edges"][i]["node"]["createdAt"]))
        str_ultimaModificacion = result["data"]["search"]["edges"][i]["node"]["updatedAt"]
        ultimaModificacion.append(date_time_formatter(str_ultimaModificacion))
        tiempoModificacion.append(date_time_until_now(str_ultimaModificacion))
        str_ultimoCommit = result["data"]["search"]["edges"][i]["node"]["defaultBranchRef"]["target"]["history"]["edges"][0]["node"]["committedDate"]
        ultimoCommit.append(date_time_formatter(str_ultimoCommit))
        tiempoCommit.append(date_time_until_now(str_ultimoCommit))

    ranges = (pd.DataFrame(columns=['NULL'], index=pd.date_range(datetime.now()-timedelta(hours=8), datetime.now(), freq='10T'))
       .index.strftime('%d/%m/%Y %H:%M:%S')
       .tolist()
    )

    cuentasM = [0]*(len(ranges)-1)
    cuentasC = [0]*(len(ranges)-1)

    for i in ultimaModificacion:
        for j in range(len(ranges)-1):
            if(str_to_datetime(i)>str_to_datetime(ranges[j]) and str_to_datetime(i)<str_to_datetime(ranges[j+1])):
                cuentasM[j] = cuentasM[j] + 1
                break
    for i in ultimoCommit:
        for j in range(len(ranges)-1):
            if(str_to_datetime(i)>str_to_datetime(ranges[j]) and str_to_datetime(i)<str_to_datetime(ranges[j+1])):
                cuentasC[j] = cuentasC[j] + 1
                break
    
    ranges2 = []
    m=0
    for i in range(len(ranges)-1):
        var = i*10
        if(var==0): ranges2.append("["+str(m)+"h0m"+" - "+str(m)+"h"+str(var%60+10)+"m"+"]")
        else:
            if(var%60==0):
                m = m + 1
                ranges2.append("["+str(m)+"h"+" - "+str(m)+"h"+str(var%60+10)+"m"+"]")
            else:
                if(var%60==50):
                    ranges2.append("["+str(m)+"h"+str(var%60)+"m - "+str(m+1)+"h]")
                else:
                    ranges2.append("["+str(m)+"h"+str(var%60)+"m - "+str(m)+"h"+str(var%60+10)+"m]")
    
    grafica = zip(ranges2,list(reversed(cuentasM)),list(reversed(cuentasC)))

    return [propietarios,nombres,fechaCreacion,ultimaModificacion,tiempoModificacion,ultimoCommit,tiempoCommit,grafica]  


def get_evolucion_repositorios_coronavirus(fechas,str_fecha):
    query = """
    {
    search(query: "topic:covid-19 sort:updated-asc stars:>1 created:>%s", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            name
            owner {
                login
            }
            createdAt
            }
        }
        }
    }
    }
    """ % str_fecha   

    result = run_query(query) # Execute the query
    num_results = int(result["data"]["search"]["repositoryCount"])
    print(num_results)
    if(num_results>100):
        num_results = 100
    nombres = []
    fechaCreacion = []
    ids = [0]
    propietarios = []

    for i in range(num_results):
        createdAt = result["data"]["search"]["edges"][i]["node"]["createdAt"]
        if(i==num_results-1 and len(ids)<2800):
            lista = get_evolucion_repositorios_coronavirus(fechaCreacion,str(createdAt))
            nombres.extend(lista[0])
            fechaCreacion.extend(lista[1])
            ids.extend(np.add(lista[2], 100).tolist())
            propietarios.extend((lista[3]))
        else:
            nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
            fechaCreacion.append(date_time_formatter(createdAt))
            ids.append(ids[len(ids)-1]+1)
            propietarios.append(result["data"]["search"]["edges"][i]["node"]["owner"]["login"])

    ranges = (pd.DataFrame(columns=['NULL'], index=pd.date_range(datetime(2019,11,30), datetime.now()+timedelta(60), freq='M'))
       .index.strftime('%d/%m/%Y %H:%M:%S')
       .tolist()
    )
    str_ranges = (pd.DataFrame(columns=['NULL'], index=pd.date_range(datetime(2019,11,30), datetime.now()+timedelta(60), freq='M'))
       .index.strftime('%B/%Y')
       .tolist()
    )

    cuentas = [0]*(len(ranges)-1)

    for i in fechaCreacion:
        for j in range(len(ranges)-1):
            if(str_to_datetime(i)>str_to_datetime(ranges[j]) and str_to_datetime(i)<str_to_datetime(ranges[j+1])):
                cuentas[j] = cuentas[j] + 1
                break


    grafica = [ranges,str_ranges,cuentas]

    return [nombres,fechaCreacion,ids,propietarios,grafica]


def get_repositorios_coronavirus_mas_proyectos(fechas,str_fecha):
    query = """
    {
    search(query: "topic:covid-19 sort:updated-desc created:<%s", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
            node {
            ... on Repository {
            owner {
                login
            }
            name
            createdAt
            projects(first: 10) {
                nodes {
                    name
                }
            }
            }
        }
        }
    }
    }
    """ % (str_fecha)

    result = run_query(query) # Execute the query
    num_results = int(result["data"]["search"]["repositoryCount"])
    print(num_results)
    if(num_results>100):
        num_results = 100
    nombres = []
    propietarios = []
    fechaCreacion = fechas
    proyectos = []
    ids = [0]

    for i in range(num_results):
        createdAt = result["data"]["search"]["edges"][i]["node"]["createdAt"]
        str_fecha_after = str(str_fecha_after_generator(str_fecha).isoformat())
        if(i==num_results-1 and len(ids)<200 and str_fecha_after_generator(str_fecha)<datetime.now().astimezone(UTC)):
            lista = get_repositorios_coronavirus_mas_proyectos(fechaCreacion,str_fecha_after)
            nombres.extend(lista[0])
            propietarios.extend(lista[1])
            fechaCreacion = lista[2]
            proyectos.extend(lista[3])
            ids.extend(np.add(lista[4], len(ids)).tolist())
        
        else:
            projects = result["data"]["search"]["edges"][i]["node"]["projects"]["nodes"]
            projects_by_rep = []    
            for j in range(len(projects)):
                projects_by_rep.append(projects[j]["name"])
            if(len(projects_by_rep)>0 and (str(date_time_formatter(createdAt)) not in fechaCreacion) and str_to_datetime(date_time_formatter(createdAt))>datetime(2019,12,30)):
                nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
                propietarios.append(result["data"]["search"]["edges"][i]["node"]["owner"]["login"])
                proyectos.append(projects_by_rep)
                fechaCreacion.append(date_time_formatter(createdAt))
                ids.append(ids[len(ids)-1]+1)

    return [nombres,propietarios,fechaCreacion,proyectos,ids]

def get_information_from_repository(name, owner):
    query = """
    {
    repositoryOwner(login:"%s") {
        repository(name:"%s") {
            name
            url
            description
            owner {
                avatarUrl
                ...on User {
                    location
                }
            }
            createdAt
            isFork
            parent {
                name
            }
            languages(first: 10) {
                totalCount
                nodes {
                name
                }
            }
            labels(first: 10) {
                totalCount
                nodes {
                name
                }
            }
            projects(first: 10) {
                totalCount
                nodes {
                name
                }
            }
            pushedAt
            updatedAt
            watchers {
                totalCount
            }
            stargazers {
                totalCount
            }
            forks {
                totalCount
            }
            }
        }
    }
    """ % (owner, name)

    result = run_query(query) # Execute the query
    print(result)

    print(len(result["data"]["repositoryOwner"]["repository"]["languages"]["nodes"]))


    foto = result["data"]["repositoryOwner"]["repository"]["owner"]["avatarUrl"]
    url = result["data"]["repositoryOwner"]["repository"]["url"]
    fechaCreacion = date_time_formatter(result["data"]["repositoryOwner"]["repository"]["createdAt"])
    nombre = name
    descripcion = result["data"]["repositoryOwner"]["repository"]["description"]
    propietario = owner
    location = "No ha sido asignada"
    if("location" in result["data"]["repositoryOwner"]["repository"]["owner"]):
        if(result["data"]["repositoryOwner"]["repository"]["owner"]["location"] is not None):
            location = result["data"]["repositoryOwner"]["repository"]["owner"]["location"] + " - (" + from_local_to_country(result["data"]["repositoryOwner"]["repository"]["owner"]["location"]) + ")"
    isForked = result["data"]["repositoryOwner"]["repository"]["isFork"]
    if(bool(isForked)):
        isForked = "Sí"
        parent = result["data"]["repositoryOwner"]["repository"]["parent"]
    else: 
        isForked = "No"
        parent = "No procede, puesto que es un repositorio original"
    languages = []
    for i in range(len(result["data"]["repositoryOwner"]["repository"]["languages"]["nodes"])):
        languages.append(result["data"]["repositoryOwner"]["repository"]["languages"]["nodes"][i]["name"])
    labels = []
    for i in range(len(result["data"]["repositoryOwner"]["repository"]["labels"]["nodes"])):
        labels.append(result["data"]["repositoryOwner"]["repository"]["labels"]["nodes"][i]["name"])
    num_proyectos = result["data"]["repositoryOwner"]["repository"]["projects"]["totalCount"]
    proyectos = []
    for i in range(num_proyectos):
        proyectos.append(result["data"]["repositoryOwner"]["repository"]["projects"]["nodes"][i]["name"])
    last_push = date_time_formatter(result["data"]["repositoryOwner"]["repository"]["pushedAt"])
    last_update = date_time_formatter(result["data"]["repositoryOwner"]["repository"]["updatedAt"])
    watchers = result["data"]["repositoryOwner"]["repository"]["watchers"]["totalCount"]
    stars = result["data"]["repositoryOwner"]["repository"]["stargazers"]["totalCount"]
    forks = result["data"]["repositoryOwner"]["repository"]["forks"]["totalCount"]
    
    return [foto,url,nombre,propietario,location,isForked,languages,labels,num_proyectos,proyectos,last_push,last_update,watchers,stars,forks,parent,fechaCreacion,descripcion]


def get_paises_mas_repositorios():
    query = """
        {
    search(query: "topic:covid-19 stars:>100", type: REPOSITORY, first: 100) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            owner {
                ... on User {
                location
                }
            }
            updatedAt
            }
        }
        }
    }
    }
    """

    result = run_query(query) # Execute the query
    num_results = int(result["data"]["search"]["repositoryCount"])
    print(num_results)
    if(num_results>100):
        num_results = 100
    paises = []

    for i in range(num_results):
        localidad = result["data"]["search"]["edges"][i]["node"]["owner"]
        if(len(localidad)>0):
            pais = from_local_to_country(result["data"]["search"]["edges"][i]["node"]["owner"]["location"])
            if(pais is not None):
                paises.append(pais)

    return paises

#==============
# Otros métodos
#==============

def date_time_formatter(str_datetime) :
    fecha = dateutil.parser.isoparse(str_datetime)+timedelta(0,7200)
    return fecha.strftime('%d/%m/%Y %H:%M:%S')

def str_to_datetime(str_datetime):
    return datetime.strptime(str_datetime, '%d/%m/%Y %H:%M:%S')

def str_fecha_after_generator(str_datetime):
    fecha = dateutil.parser.isoparse(str_datetime)
    return fecha + timedelta(days=50)

def str_fecha_before_generator(str_datetime):
    fecha = dateutil.parser.isoparse(str_datetime)
    return fecha - timedelta(days=20)

def days_until_now(str_datetime):
    fecha = dateutil.parser.isoparse(str_datetime)
    result = (date.today() - fecha.date()).days
    return result

def date_time_until_now(str_datetime):
    fecha = dateutil.parser.isoparse(str_datetime)
    result = (datetime.now().astimezone(UTC)) - fecha
    str_result = str(result).split(":")
    return str_result[0].replace("days","días") + "h " + str_result[1] + "min y " + str_result[2].split(".")[0] + "seg"

def from_local_to_country(str_local):
    geolocator = Nominatim(user_agent="covid19analyzer")
    location = geolocator.geocode(str_local)
    if (location is not None):
        localidad = location.address
        localidad_partes = localidad.split(",")
        pais = localidad_partes[len(localidad_partes)-1].strip()
        return pais
    else:
        return None
