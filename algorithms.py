# Implement required data structures here to parse the recommendations (list of movie objects)
import api
from movie import Movie

def get_similarity(m1, m2):
    m1_genres = set(m1.to_dict()["genre_ids"])
    m2_genres = set(m2.to_dict()["genre_ids"])

    #print("movie 1: "+", ".join(map(str, m1_genres)))
    #print("movie 2: "+", ".join(map(str, m2_genres)))

    m1_director = set(api.get_more_info(m1.to_dict()["id"])["director"])
    m2_director = set(api.get_more_info(m2.to_dict()["id"])["director"])

    union_genres = m1_genres | m2_genres
    intersect_genres = m1_genres & m2_genres

    union_directors = m1_director | m2_director
    intersect_directors = m1_director & m2_director

    genre_similarity = len(intersect_genres) / len(union_genres) if len(union_genres) > 0 else 0
    director_similarity = len(intersect_directors) / len(union_directors) if len(union_directors) > 0 else 0

    #return str(director_similarity)
    #return str(genre_similarity)
    return str(float((genre_similarity  + director_similarity ) / 2))
    #return str(len(set(m1_genres) & set(m2_genres)) / len(set(m1_genres) | set(m2_genres))) 
