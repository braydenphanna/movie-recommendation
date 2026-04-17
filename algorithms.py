# Implement required data structures here to parse the recommendations (list of movie objects)
from movie import Movie

def get_similarity(m1, m2):
    m1_genres = m1.to_dict()["genre_ids"]
    m2_genres = m2.to_dict()["genre_ids"]
    print("movie 1: "+", ".join(map(str, m1_genres)))
    print("movie 2: "+", ".join(map(str, m2_genres)))

    return str(len(set(m1_genres) & set(m2_genres)) / len(set(m1_genres) | set(m2_genres)))
