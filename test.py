from flask import Flask
from flask import render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/scripts')
def scripts():
    return render_template('scripts.html')

@app.route('/data')
def data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)