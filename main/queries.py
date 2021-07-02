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
    visualizaciones = []
    for i in range(num_results):
        ids.append(result["data"]["search"]["edges"][i]["node"]["id"])
        nombres.append(result["data"]["search"]["edges"][i]["node"]["name"])
        fechaCreacion.append(date_time_formatter(result["data"]["search"]["edges"][i]["node"]["createdAt"]))
        visualizaciones.append(result["data"]["search"]["edges"][i]["node"]["watchers"]["totalCount"])
    return [ids,nombres,fechaCreacion,visualizaciones]  

    # id = [result["data"]["search"]["edges"][i]["node"]["id"]]
    #     nombre = [result["data"]["search"]["edges"][i]["node"]["name"]]
    #     fechaCreacion = [result["data"]["search"]["edges"][i]["node"]["createdAt"]]
    #     visualizaciones = [result["data"]["search"]["edges"][i]["node"]["watchers"]["totalCount"]]
    #     repositorio = Repositorio(id=id,nombre=nombre, fechaCreacion=fechaCreacion, visualizaciones=visualizaciones)
    #     listaDeRepositorios.append(repositorio)
    # return listaDeRepositorios



#==============
# Otros métodos
#==============

def date_time_formatter(datetime) :
    datetime2 = dateutil.parser.isoparse(datetime)
    return datetime2.strftime('%d/%m/%Y %H:%M:%S')