from flask import Flask, request, render_template
app = Flask(__name__)
import strings

# app.secret_key = 'this-should-be-something-unguessable'

@app.route('/')
def index():
    return render_template('index.html', strings=strings)

@app.route('/research')
def research():
    return render_template('research.html')


if __name__ == "__main__":
    app.run(debug=True)

