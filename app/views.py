from app import app
from flask import render_template

#@app.route('/')
@app.route('/index')
def index():
  return "Hello World"


# source of comment: https://pythonprogramming.net/jquery-flask-tutorial/
@app.route('/interactive/')
def interactive():

    return render_template('interactive.html')
