import requests
import json
from movie import Movie

# Enter an api key here
api_key=""

headers = {
    "accept": "application/json",
    "Authorization": "Bearer "+ api_key
}

# Takes a TMDB ID and a number of results (up to 20)
def get_recommendations(query, num): 
    # make sure num isn't over 20
    if(num>20): num=20

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
    for n in range(num):
        movies.append(Movie.from_json(n))

    return movies

# Gets more movie info for a specific movie (credits and imdb id)
def get_more_info(query):
    url = "https://api.themoviedb.org/3/movie/"+str(query)+"/credits?language=en-US"
    credits = requests.get(url, headers=headers).json()
    url = "https://api.themoviedb.org/3/movie/"+str(query)+"/external_ids"
    ext_ids = requests.get(url, headers=headers).json()

    extra_info = {
        "director": [member for member in credits['crew'] if member['job'] == 'Director'][0]["name"],
        "cast": [member['name'] for member in credits.get('cast', [])[:10]],
        "imdb": "https://www.imdb.com/title/"+ext_ids['imdb_id']
    }

    return extra_info