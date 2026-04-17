from flask import Flask, render_template, request,jsonify
import api
import algorithms
from movie import Movie

app = Flask(__name__)

recommendations = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations/', methods=['GET', 'POST'])
def recommend():
    global recommendations

    query = request.values.get('query')

    if not query:
        return "Missing query parameter", 400

    recommendations = api.get_recommendations(query, 15)
    return render_template('recommendations.html', recommendations=recommendations)

@app.route('/moreinfo/<id>')
def more_info(id):
    return api.get_more_info(id)

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