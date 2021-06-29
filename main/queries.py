from graphene import ObjectType, String, Schema
import requests

headers = {"Authorization": "token 7efc823e322b745df4ef31c4e95ff44327a029f3"}


#INICIO

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.

    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        print(request.json())
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def get_repositories_coronavirus():

    query = """
    {
    search(query: "name:covid sort:asc", type: REPOSITORY, first: 100 ) {
        repositoryCount
        edges {
            node {
            ... on Repository {
            id
            name
            createdAt
            issues {
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
    print(num_results)
    if(num_results>100):
        num_results = 100
    print(num_results)
    ids = []
    nombres = []
    creaciones = []
    d = dict()
    lista = []
    for i in range(num_results):
        d["ids"] = [result["data"]["search"]["edges"][i]["node"]["id"]]
        d["nombres"] = [result["data"]["search"]["edges"][i]["node"]["name"]]
        d["creaciones"] = [result["data"]["search"]["edges"][i]["node"]["createdAt"]]
        lista = lista+d["ids"]+d["nombres"]+d["creaciones"]
    return lista

