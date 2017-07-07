from app import api
from flask_restful import Resource
from flask import request
from app import app
from flask import render_template

player1 = [0,50]
player2 = [100,50]
ball = [50,50]

class PlayerMoves(Resource):
    def get(self, playernum):
        if playernum == 1:
          return {playernum: player1}
        if playernum == 2:
          return {playernum: player2}
        else: return {-1: -1}

    def put(self, playernum):
        direction = request.form['data']
        if playernum == '1':
          if direction > 0:
            player1[1] = player1[1] + 1
          else:
            player1[1] = player1[1] - 1
          return {playernum: player1}
        if playernum == '2':
          if direction < 0:
            player2[1] = player2[1] + 1
          else:
            player2[1] = player2[1] - 1
          return {playernum: player2}
        return {-1: -1}

api.add_resource(PlayerMoves, '/<string:playernum>')

# source of comment: https://pythonprogramming.net/jquery-flask-tutorial/
@app.route('/interactive/')
def interactive():
    return render_template('interactive.html')


@app.route('/dopplerInput/')
def dopplerInput():
    return render_template( 'doppler-example.html' )
