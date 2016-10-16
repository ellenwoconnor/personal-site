from flask import Flask, request, render_template
app = Flask(__name__)

# app.secret_key = 'this-should-be-something-unguessable'

@app.route('/')
def index():
    return render_template('index.html', strings=strings, current_page='about')

@app.route('/research')
def research():
    return render_template('research.html', current_page='research')

@app.route('/resume')
def resume():
    return render_template('resume.html', current_page='resume')


if __name__ == "__main__":
    app.run(debug=True)

