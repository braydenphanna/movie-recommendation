import requests
import json
from movie import Movie
import algorithms

# Enter an api key here
api_key=""

headers = {
    "accept": "application/json",
    "Authorization": "Bearer "+ api_key
}

# Takes a TMDB ID and a number of results (up to 20)
def get_recommendations(id, num):
    num = min(num, 20)
    movies = []

    # Get main movie
    movie_url = "https://api.themoviedb.org/3/movie/"+id+"?language=en-US"
    movie_data = requests.get(movie_url, headers=headers).json()
    movies.append(Movie.from_json(movie_data))

    # Get recommendations
    rec_url = "https://api.themoviedb.org/3/movie/"+id+"/recommendations?language=en-US&page=1"
    rec_data = requests.get(rec_url, headers=headers).json()

    for entry in rec_data.get("results", [])[:num]:
        movies.append(Movie.from_json(entry))

    return movies

# Gets more movie info for a specific movie
def get_more_info(query):
    url = "https://api.themoviedb.org/3/movie/"+str(query)+"/credits?language=en-US"
    credits = requests.get(url, headers=headers).json()
    url = "https://api.themoviedb.org/3/movie/"+str(query)+"?language=en-US"
    details = requests.get(url, headers=headers).json()

    extra_info = {
        "director": [member["name"] for member in [member for member in credits['crew'] if member['job'] == 'Director']],
        "tagline": details['tagline'],
        "movieCast": [member['name'] for member in credits.get('cast', [])],
        "movieCast_images": [member['profile_path'] for member in credits.get('cast', [])],
        "movieCast_characters": [member['character'] for member in credits.get('cast', [])],
        "movieCrew": [member['name'] for member in credits.get('crew', [])],
        "movieCrew_images": [member['profile_path'] for member in credits.get('crew', [])],
        "movieCrew_jobs": [member['job'] for member in credits.get('crew', [])],
        "genres": [member['name'] for member in details.get('genres', [])],
        "details": ["<b>Runtime:</b> " +str(details['runtime'])+" mins", 
                    "<b>Release Date:</b> " +str(details['release_date']),
                    "<b>Production Companies:</b><br>" +"<br>".join([member['name'] for member in details.get('production_companies', [])])],
        "imdb": "https://www.imdb.com/title/"+details['imdb_id']
    }

    return extra_info

cache = {}

# Gets raw details for a movie, used for similarity calculations
def get_raw_details(id):
    if id in cache:
        return cache[id]

    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    details = requests.get(url, headers=headers).json()

    cache[id] = details
    return details

# Search for movies by name, return list of movie objects
def search(query):
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page=1"
    data = requests.get(url, headers=headers).json()

    movies = []

    results = data.get("results", [])
    for entry in results[:10]:  # limit to 10 safely
        movies.append(Movie.from_json(entry).to_dict())

    return movies

# Set a new API key, used for the form on the index page
def set_key(key):
    global api_key
    api_key = key
    
    global headers 
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "+ api_key
    }

# Test if an API key is valid by making a simple request to the popular movies endpoint
def test_key(key):
    url = f"https://api.themoviedb.org/3/movie/popular"
    response = requests.get(url, headers={
        "accept": "application/json",
        "Authorization": "Bearer "+ key
    })

    if response.status_code == 200:
        return True
    else:
        return False
