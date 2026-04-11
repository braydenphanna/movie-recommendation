import requests
import json
from movie import Movie

def search(query): 
    # Enter the api key
    api_key="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMzA0MmNlYjZhYzViMDcyNWFlMDU1MDBmNjkwNGQ3MyIsIm5iZiI6MTc3NTc2Njg4MS45NTYsInN1YiI6IjY5ZDgwZDYxYjRlN2M1NDg0ZDEyNzAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2qlBefys4nPjWRH_dgZsPq1MjtcBtiGERo3Rb0i-7Zw"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "+ api_key
    }

    movies=[]

    # Get corresponding movie ID
    url = "https://api.themoviedb.org/3/search/movie?query="+query+"&include_adult=false&language=en-US&page=1"
    search_results = requests.get(url, headers=headers)
    id = search_results.json()["results"][0]["id"]

    # Add starting movie to movies list at index 0
    with open("recommendations.json", "w") as file:
        json.dump(search_results.json(), file, indent=4)
    movies.append(Movie.from_json(0))

    # Write similar movie recommendations to recommendations.json
    url = "https://api.themoviedb.org/3/movie/"+str(id)+"/recommendations?language=en-US&page=1"
    recommendations = requests.get(url, headers=headers)

    # Add 20 recommended movies to movies list at indeces 1-21
    with open("recommendations.json", "w") as file:
        json.dump(recommendations.json(), file, indent=4)
    for n in range(20):
        movies.append(Movie.from_json(n))

    return movies
