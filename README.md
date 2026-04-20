# &#x1F578;&#xFE0E; CineWeb
A web-based application that employs graph data structures to generate a web of movie recommendations based on your last watch.
## Demo
[Click here](https://cineweb.pythonanywhere.com) to try the web demo.
## Usage
1. Install the required python libraries
```shell
pip install flask requests
```
2. Start the server
```shell
python3 ./server.py
```
3. [Click here](http://127.0.0.1:8000) to access the site
4. Input a valid TMDB API Key using the button in the top right corner of the home page
## Objectives
### Scripts
- [x] Create function(s) to interface with [TMDB API](https://developer.themoviedb.org/docs/getting-started) (use /search -> /recommendations; will output a specified amount of recommended movies in a json file)
- [x] Make a movie class (include most of the attributes that the json includes)
- [x] Create a function to parse each movie entry in the outputted json file into individual movie objects
- [X] Create a simple algorithm to rank the movies using and put them in a weighted graph
- [ ] Create a more complex algorithm to rank the movies using and put them in a weighted graph (based on info such as: genre crossover, director, and lead actors)
- [ ] Create a rating System for each movie?
- [ ] Create a watched list
- [ ] Create a like/ dislike system for each watched movie?

### User Interface
- [x] Basic flask setup with working connectivity
- [X] Display the recommendation web with movie posters from TMDB 
- [X] Hover over to see movie details preview?
- [X] Add more info to side menu (add director, cast, imdb) 
- [X] Zoom into a movie when selected
- [X] Give graph labeled edges (denoting similarity)
- [X] Add option to input API key on the website
- [X] Make everyting look more appealing (change colors, fonts, etc.)
- [ ] Offer suggested searches while entering your starting movie

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

