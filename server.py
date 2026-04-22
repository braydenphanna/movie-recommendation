from flask import Flask, render_template, request,jsonify
import api
import algorithms
from movie import Movie

app = Flask(__name__)

recommendations = []

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', valid=api.test_key(api.api_key))

@app.route('/recommendations/<id>', methods=['GET', 'POST'])
def recommend(id):
    global recommendations

    if not id:
        return render_template('index.html', valid=api.test_key(api.api_key), error="Empty Query")

    if not api.test_key(api.api_key):
        return render_template('index.html', valid=api.test_key(api.api_key), error="Invalid API Key")

    recommendations = api.get_recommendations(id, 10)
    return render_template('recommendations.html', recommendations=recommendations)

@app.route('/more_recommendations/<id>')
def more_recommendations(id):
    movies = api.get_recommendations(id, 5)
    return jsonify([m.to_dict() for m in movies])

@app.route('/moreinfo/<id>')
def more_info(id):
    return api.get_more_info(id)

@app.route('/search/<name>')
def search(name):
    return api.search(name)

@app.route('/getsimilarity/<id1>/<id2>')
def get_similarity(id1,id2):
    print(id1)
    print(id2)
    return algorithms.get_similarity(recommendations[int(id1)],recommendations[int(id2)])

@app.route('/setapikey/', methods=['GET', 'POST'])
def set_api_key():
    key = request.form.get('apikey')
    valid=api.test_key(key)
    if(valid):api.set_key(key)
    return render_template('index.html', valid=valid)

if __name__ == '__main__':
    app.run(debug=True,port=8000)