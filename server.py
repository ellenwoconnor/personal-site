import os
from flask import Flask, request, render_template

app = Flask(__name__)

# app.secret_key = 'this-should-be-something-unguessable'

@app.route('/')
def about():
    return render_template('about.html', current_page='about')

@app.route('/research')
def research():
    return render_template('research.html', current_page='research')

@app.route('/resume')
def resume():
    return render_template('resume.html', current_page='resume')

@app.route('/odyssey')
def odyssey():
    return render_template('odyssey.html', current_page='odyssey')


if __name__ == "__main__":
    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
