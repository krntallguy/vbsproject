from app import api
from flask_restful import Resource
from flask import request
from app import app
from flask import render_template

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
api.add_resource(TodoSimple, '/<string:todo_id>')



# source of comment: https://pythonprogramming.net/jquery-flask-tutorial/
@app.route('/interactive/')
def interactive():
     return render_template('interactive.html')
