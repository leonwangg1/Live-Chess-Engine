from flask import Markup, Flask, render_template, Response, url_for
import cv2
from chess_stuff import stockfish_test
import chess.svg
import chess
import datetime
import time
import threading

board = stockfish_test.board
app = Flask(__name__)

lock = threading.Lock()

@app.route('/')
def main():
    return render_template("test.html")

@app.route('/board')
def board_feed():
    global board
    return Response(get_board(board),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
def get_board(board):
  while True:
    svg = chess.svg.board(board, size=400)
    yield ('--frame\r\n'
                'Content-Type: image/svg+xml\r\n\r\n' + svg + '\r\n')
    time.sleep(1)

@app.route('/update')
def update():
  board.push(stockfish_test.engine.play(board, chess.engine.Limit(time=1)).move)
  return {"status": "success"}
   
@app.route('/stream',methods = ['GET'])
def stream():
   return Response(generate(), mimetype = "multipart/x-mixed-replace; boundary=frame")

def generate():
   # grab global references to the lock variable
   global lock
   # initialize the video stream
   vc = cv2.VideoCapture(0)
   
   # check camera is open
   if vc.isOpened():
      rval, frame = vc.read()
   else:
      rval = False

   # while streaming
   while rval:
      # wait until the lock is acquired
      with lock:
         # read next frame
         rval, frame = vc.read()
         # if blank frame
         if frame is None:
            continue

         # encode the frame in JPEG format
         (flag, encodedImage) = cv2.imencode(".jpg", frame)

         # ensure the frame was successfully encoded
         if not flag:
            continue

      # yield the output frame in the byte format
      yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
   # release the camera
   vc.release()
   
app.run()