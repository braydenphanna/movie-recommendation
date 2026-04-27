# Implement required data structures here to parse the recommendations (list of movie objects)
from collections import defaultdict
import csv

import api
from movie import Movie

def get_similarity(m1, m2):
    m1_genres = set(m1.to_dict()["genre_ids"])
    m2_genres = set(m2.to_dict()["genre_ids"])

    #print("movie 1: "+", ".join(map(str, m1_genres)))
    #print("movie 2: "+", ".join(map(str, m2_genres)))

    #m1_director = set(api.get_more_info(m1.to_dict()["id"])["director"])
    #m2_director = set(api.get_more_info(m2.to_dict()["id"])["director"])

    m1_rating = set([m1.to_dict()["vote_average"]])
    m2_rating = set([m2.to_dict()["vote_average"]])

    union_genres = m1_genres | m2_genres
    intersect_genres = m1_genres & m2_genres

    #union_directors = m1_director | m2_director
    #intersect_directors = m1_director & m2_director

    union_rating = m1_rating | m2_rating
    intersect_rating = m1_rating & m2_rating

    #genre_similarity = len(intersect_genres) / len(union_genres) if len(union_genres) > 0 and else 0

    intersect_sum = 0
    for genre in intersect_genres:
        if genre in m1_genres and genre in m2_genres:
            intersect_sum+= 1
            if len(intersect_genres) == len(m1_genres):
                genre_similarity = 1
            else:
                genre_similarity = len(intersect_genres) / len(union_genres) if len(union_genres) > 0 else 0

    #director_similarity = len(intersect_directors) / len(union_directors) if len(union_directors) > 0 else 0
    print(m2_rating)
    rating_factor = float(m2_rating.pop()) /10

    #print(str(director_similarity))
    #print("m1: " + str(m1_rating))
    #print("m2: " + str(m2_rating))
    print("union_genres: " + str(union_genres))
    print("intersect_genres: " + str(intersect_genres))
    #print("rating sim : " + str(rating_factor))
    #print(f"Genre Similarity: {genre_similarity:.2f}")
    return str(float((genre_similarity +  rating_factor ) / 2))
    #return str(len(set(m1_genres) & set(m2_genres)) / len(set(m1_genres) | set(m2_genres))) 

# Imports the ratings.csv file from letterboxd and returns a dictionary of movies and their ratings.
def LetterBoxd_Import():
    movies = defaultdict(list)

    with open('letterboxd/ratings.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            title = row.get('Name') 
            rating = row.get('Rating') 

            if not title:
                continue
            
            # creates a dict of movie: bool - True if the rating is 3 or above, False otherwise        
            if float(rating) >= 3:    
                movies[title]= True
            else:
                movies[title]= False

    return movies