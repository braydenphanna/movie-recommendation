import requests
import json
from movie import Movie

def search(query): 
    # Enter the api key
    api_key=""

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "+ api_key
    }

    # Get corresponding movie ID
    url = "https://api.themoviedb.org/3/search/movie?query="+query+"&include_adult=false&language=en-US&page=1"
    search_results = requests.get(url, headers=headers)
    id = search_results.json()["results"][0]["id"]

    # Write similar movie recommendations to recommendations.json
    url = "https://api.themoviedb.org/3/movie/"+str(id)+"/recommendations?language=en-US&page=1"
    recommendations = requests.get(url, headers=headers)
    with open("recommendations.json", "w") as file:
        json.dump(recommendations.json(), file, indent=4)

    movies=[]
    for n in range(20):
        movies.append(Movie.from_json(n))

    return movies
