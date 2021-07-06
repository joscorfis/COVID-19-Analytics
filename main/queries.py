from dateutil.tz import UTC
from graphene import ObjectType, String, Schema
from datetime import date, datetime, timedelta, timezone
import dateutil.parser
import requests
import json
import pandas as pd

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
            id
            name
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
    ids = []
    nombres = []
    fechaCreacion = []
    observadores = []
    porcentajes = []
    for i in range(num_results):
        ids.append(result["data"]["search"]["edges"][i]["node"]["id"])
        nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
        fechaCreacion.append(date_time_formatter(result["data"]["search"]["edges"][i]["node"]["createdAt"]))
        observadores.append(result["data"]["search"]["edges"][i]["node"]["watchers"]["totalCount"])
        if(i<1):
            max_observadores = observadores[0]
            porcentajes.append(100)
        else:
            porcentajes.append((result["data"]["search"]["edges"][i]["node"]["watchers"]["totalCount"]/max_observadores)*100)
    return [ids,nombres,fechaCreacion,observadores,porcentajes]  


def get_repositorios_coronavirus_mas_forks():

    query = """
    {
    search(query: "topic:covid-19 forks:>=60", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            id
            name
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
    ids = []
    nombres = [] 
    fechaCreacion = []
    forks = [] 
    porcentajes = []
    for i in range(num_results):
        ids.append(result["data"]["search"]["edges"][i]["node"]["id"])
        nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
        fechaCreacion.append(date_time_formatter(result["data"]["search"]["edges"][i]["node"]["createdAt"]))
        forks.append(result["data"]["search"]["edges"][i]["node"]["forks"]["totalCount"])
        if(i<1):
            max_forks = forks[0]
            porcentajes.append(100)
        else:
            porcentajes.append((result["data"]["search"]["edges"][i]["node"]["forks"]["totalCount"]/max_forks)*100)

    return [ids,nombres,fechaCreacion,forks,porcentajes]  


def get_repositorios_coronavirus_mas_estrellas():

    query = """
    {
    search(query: "topic:covid-19 stars:>=160", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            id
            name
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
    ids = []
    nombres = [] 
    fechaCreacion = []
    estrellas = [] 
    porcentajes = []
    for i in range(num_results):
        ids.append(result["data"]["search"]["edges"][i]["node"]["id"])
        nombres.append(str(result["data"]["search"]["edges"][i]["node"]["name"]))
        fechaCreacion.append(date_time_formatter(result["data"]["search"]["edges"][i]["node"]["createdAt"]))
        estrellas.append(result["data"]["search"]["edges"][i]["node"]["stargazers"]["totalCount"])
        if(i<1):
            max_stars = estrellas[0]
            porcentajes.append(100)
        else:
            porcentajes.append((result["data"]["search"]["edges"][i]["node"]["stargazers"]["totalCount"]/max_stars)*100)

    return [ids,nombres,fechaCreacion,estrellas,porcentajes] 


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
            id
            name
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
    ids = []
    nombres = []
    fechaCreacion = []
    tiempo = []
    for i in range(num_results):
        createAt = result["data"]["search"]["edges"][i]["node"]["createdAt"]
        if dateutil.parser.isoparse(createAt).date() > date(2019,12,31):
            ids.append(result["data"]["search"]["edges"][i]["node"]["id"])
            nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
            fechaCreacion.append(date_time_formatter(createAt))
            tiempo.append(days_until_now(createAt))

    return [ids,nombres,fechaCreacion,tiempo]  


def get_repositorios_coronavirus_mas_actualizados():

    query = """
    {
    search(query: "topic:covid-19 sort:updated-desc stars:>1", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
        node {
            ... on Repository {
            id
            name
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
    ids = []
    nombres = []
    fechaCreacion = []
    ultimaModificacion = []
    tiempoModificacion = []
    ultimoCommit = []
    tiempoCommit = []
 
    for i in range(num_results):
        ids.append(result["data"]["search"]["edges"][i]["node"]["id"])
        nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
        fechaCreacion.append(date_time_formatter(result["data"]["search"]["edges"][i]["node"]["createdAt"]))
        str_ultimaModificacion = result["data"]["search"]["edges"][i]["node"]["updatedAt"]
        ultimaModificacion.append(date_time_formatter(str_ultimaModificacion))
        tiempoModificacion.append(date_time_until_now(str_ultimaModificacion))
        str_ultimoCommit = result["data"]["search"]["edges"][i]["node"]["defaultBranchRef"]["target"]["history"]["edges"][0]["node"]["committedDate"]
        if("días" in date_time_until_now(str_ultimoCommit)):
            break
        else:
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

    return [ids,nombres,fechaCreacion,ultimaModificacion,tiempoModificacion,ultimoCommit,tiempoCommit,grafica]  

#==============
# Otros métodos
#==============

def date_time_formatter(str_datetime) :
    fecha = dateutil.parser.isoparse(str_datetime)+timedelta(0,7200)
    return fecha.strftime('%d/%m/%Y %H:%M:%S')

def str_to_datetime(str_datetime):
    return datetime.strptime(str_datetime, '%d/%m/%Y %H:%M:%S')

def days_until_now(str_datetime):
    fecha = dateutil.parser.isoparse(str_datetime)
    result = (date.today() - fecha.date()).days
    return result

def date_time_until_now(str_datetime):
    fecha = dateutil.parser.isoparse(str_datetime)
    result = (datetime.now().astimezone(UTC)) - fecha
    str_result = str(result).split(":")
    return str_result[0].replace("days","días") + "h " + str_result[1] + "min y " + str_result[2].split(".")[0] + "seg"