from movie import Movie
import get_recommendations
import algorithms

# This will be the main file that the user runs
get_recommendations.search()

# Turn json entries in list of movie objects
movies=[]
for n in range(20):
    movies.append(Movie.from_json(n))

# Print recommendations to the console
print("\033[1mRecommendations:\033[0m")
print("\n".join(str(movie) for movie in movies))

# Implement graph stuff and any other graph parsing in algorithms.py and call those functions here
