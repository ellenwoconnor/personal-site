from flask import Flask, request, render_template
from time import sleep
from JobSearcher import JobSearcher

app = Flask(__name__)

# app.secret_key = 'this-should-be-something-unguessable'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/research')
def research():

    return render_template('research.html')

@app.route('/professional')
def professional():


if __name__ == "__main__":
    app.run(debug=True)
