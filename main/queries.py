from graphene import ObjectType, String, Schema
import dateutil.parser
import requests

headers = {"Authorization": "token 7efc823e322b745df4ef31c4e95ff44327a029f3"}


#INICIO

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.

    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

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

#==============
# Otros métodos
#==============

def date_time_formatter(datetime) :
    datetime2 = dateutil.parser.isoparse(datetime)
    return datetime2.strftime('%d/%m/%Y %H:%M:%S')