# Movie Recommendation App
A lightweight python application that uses graph data structures to generate a web of movie recommendations based on your last watch.
## Usage
1. Install the required python libraries
```shell
pip install flask requests
```
2. Input a TMDB api key at the top of get_recommendations.py
3. Start the server
```shell
python3 ./server.py
```
4. [Click here](http://127.0.0.1:5000) to access the site
## Objectives
### Scripts
- [x] Create function(s) to interface with [TMDB API](https://developer.themoviedb.org/docs/getting-started) (use /search -> /recommendations; will output a specified amount of recommended movies in a json file)
- [x] Make a movie class (include most of the attributes that the json includes)
- [x] Create a function to parse each movie entry in the outputted json file into individual movie objects
- [ ] Create an algorithm to rank the movies using and put them in a weighted graph (based on info such as: genre crossover, director, and lead actors)
- [ ] Create a rating System for each movie?
- [ ] Create a watched list
- [ ] Create a like/ dislike system for each watched movie?

### User Interface
- [x] Basic flask setup with working connectivity
- [X] Display the recommendation web with movie posters from TMDB 
- [X] Hover over to see movie details preview?
- [ ] Zoom into a movie when selected
- [ ] Complete the movie info side menu when (add director, cast, etc.) 
- [ ] Give graph labeled edges (denoting similarity)
- [ ] Offer suggested searches while entering your starting movie
- [ ] Add option to input API key on the website


## Tech Stack
### Frontend
- HTML
- CSS
- JavaScript
- [Vis.js](https://visjs.github.io/vis-network/docs/network/) (for displaying graphs)
### Backend
- Python 3
- [Flask](https://flask.palletsprojects.com/en/stable/) (for Python web integration)

## Other Resources
- [Flask: file system explained](https://flask.palletsprojects.com/en/stable/tutorial/layout/)
- [Flask: Python and HTML connectivity explained](https://stackoverflow.com/questions/48552343/how-can-i-execute-a-python-script-from-an-html-button)

