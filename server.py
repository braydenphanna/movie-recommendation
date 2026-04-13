from flask import Flask, render_template, request,jsonify
import get_recommendations
from movie import Movie

app = Flask(__name__)

recommendations = [...]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations/', methods=['GET', 'POST'])
def recommend():
    return render_template('recommendations.html', recommendations=get_recommendations.search(request.form['query']))

@app.route('/movie')
def movie():
    movie = Movie()
    return jsonify(movie.to_dict())

if __name__ == '__main__':
    app.run(debug=True)