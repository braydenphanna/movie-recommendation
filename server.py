from flask import Flask, render_template, request
import get_recommendations
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results/', methods=['GET', 'POST'])
def my_link():
    return render_template('results.html', results=get_recommendations.search(request.form['query']))

if __name__ == '__main__':
    app.run(debug=True)