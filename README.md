# Movie Recommendation App
A lightweight python application that uses graph data structures to generate a web of movie recommendations based on your last watch.
## Usage

```shell
python3 ./movie_recommendation.py
```
## Objectives
### Scripts
- [x] Create function(s) to interface with [TMDB API](https://developer.themoviedb.org/docs/getting-started) (use /search -> /recommendations; will output a specified amount of recommended movies in a json file)
- [x] Make a movie class (include most of the attributes that the json includes)
- [x] Create a function to parse each movie entry in the outputted json file into individual movie objects
- [ ] Create an algorithm to rank the movies using and put them in a weighted graph (based on info such as: genre crossover, director, and lead actors)
### User Interface
- [ ] Display the recommendation web with labeled edges and movie posters from TMDB (distance of edge denotes similarity?)
- [ ] Make the web interactable (hover over to see movie details preview?)
- [ ] Offer suggested searches while entering your starting movie