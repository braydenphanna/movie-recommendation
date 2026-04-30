# Implement required data structures here to parse the recommendations (list of movie objects)
from collections import defaultdict
import csv

import api
from movie import Movie

def get_similarity(m1, m2):
    m1_genres = set(m1.to_dict()["genre_ids"])
    m2_genres = set(m2.to_dict()["genre_ids"])

    m2_rating = set([m2.to_dict()["vote_average"]])

    union_genres = m1_genres | m2_genres
    intersect_genres = m1_genres & m2_genres

    intersect_sum = 0
    for genre in intersect_genres:
        if genre in m1_genres and genre in m2_genres:
            intersect_sum+= 1
            if len(intersect_genres) == len(m1_genres):
                genre_similarity = 1
            else:
                genre_similarity = len(intersect_genres) / len(union_genres) if len(union_genres) > 0 else 0

    print(m2_rating)
    rating_factor = float(m2_rating.pop()) /10
   
    print("union_genres: " + str(union_genres))
    print("intersect_genres: " + str(intersect_genres))
    
    return str(float((genre_similarity +  rating_factor ) / 2))

