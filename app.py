from operator import truediv
from re import A
from flask import Markup, Flask, render_template, Response, url_for
import cv2
from chess_stuff import stockfish_test
import chess.svg
import chess
import datetime
import time
a = 0
b = stockfish_test.board
app = Flask(__name__)
@app.route('/')
def main():
    # svg = chess.svg.board(stockfish_test.board)
    return render_template("test.html")

@app.route('/video_feed')
def video_feed():
		# Set to global because we refer the video variable on global scope, 
		# Or in other words outside the function
    global b
		# Return the result on the web
  
    return Response(abc(b),
                    mimetype='image/svg+xml; multipart/x-mixed-replace; boundary=frame')
    # return Response(chess.svg.board(b, size=400), mimetype='image/svg+xml')

@app.route('/update')
def update():
  b.push(stockfish_test.engine.play(b, chess.engine.Limit(time=1)).move)
  return {"status": "success"}

def abc(b):
  # while True:
    # board.push(stockfish_test.engine.play(board, chess.engine.Limit(time=1)).move)
  svg = chess.svg.board(b, size=400)
  # print(board)
  # return (svg)
  yield svg

def gay(a):
  while True:
    a = a + 1
    return str(a) 

@app.route('/lmao')
def lmao():
    global a
    a = a + 1
    # return Response(gay(a), mimetype="text")
    return {"now" : gay(a)}
app.run()