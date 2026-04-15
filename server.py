from flask import Flask, render_template, request,jsonify
import api
from movie import Movie

app = Flask(__name__)

recommendations = [...]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations/', methods=['GET', 'POST'])
def recommend():
    return render_template('recommendations.html', recommendations=api.get_recommendations(request.form['query'],15))

@app.route('/moreinfo/<id>')
def more_info(id):
    return api.get_more_info(id)

if __name__ == '__main__':
    app.run(debug=True,port=8000)