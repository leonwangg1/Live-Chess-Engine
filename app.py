from flask import Markup, Flask, render_template, Response, url_for
import cv2
from chess_stuff import stockfish_test
import chess.svg
import chess
import datetime
import time
import threading
import torch
import asyncio
import perspective

model = torch.hub.load('yolov5-master', 'custom', path='best.pt', source='local')
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

def classify(im):
   b = chess.Board(None)
   im = perspective.change_perspective(im)
   print("why")
   if im is None:
      return
   x, y, _ = im.shape
   boardarray = []
   x_end = -1
   for i in range(0, 8):
      x_start = x_end + 1
      x_end = x_start + x/8
      y_start = y
      row = []
      for j in range(0, 8): # (x_start, x_end), (y_start, y_end)
         y_end = y_start - y/8
         row.append([(int(x_start), int(x_end)), (int(y_end), int(y_start))])
         y_start = y_end
      boardarray.append(row)

   results = model(im)
   for i in range(0, len(results.pandas().xyxy[0])):
      piece = results.pandas().xyxy[0].iloc[i]
      w = (piece["xmin"] + piece["xmax"])/2
      h = (piece["ymin"] + piece["ymax"])/2
      for x in range(0, 8):
         for y in range(0, 8):
               xs = boardarray[x][y][0][0]
               xe = boardarray[x][y][0][1]
               ys = boardarray[x][y][1][0]
               ye = boardarray[x][y][1][1]
               if w >= xs and w <= xe and h >= ys and h <= ye:
                  square = chess.square(x, y)
                  name = piece["name"]
                  if name == "black-rook":
                     cpiece = chess.Piece(chess.ROOK, chess.BLACK)
                     b.set_piece_at(chess.square(x, y), cpiece)
                  if name == "black-queen":
                     cpiece = chess.Piece(chess.QUEEN, chess.BLACK)
                     b.set_piece_at(chess.square(x, y), cpiece)
                  if name == "black-bishop":
                     cpiece = chess.Piece(chess.BISHOP, chess.BLACK)
                     b.set_piece_at(chess.square(x, y), cpiece)
                  if name == "black-knight":
                     cpiece = chess.Piece(chess.KNIGHT, chess.BLACK)
                     b.set_piece_at(chess.square(x, y), cpiece)
                  if name == "black-pawn":
                     cpiece = chess.Piece(chess.PAWN, chess.BLACK)
                     b.set_piece_at(chess.square(x, y), cpiece)
                  if name == "black-king":
                     cpiece = chess.Piece(chess.KING, chess.BLACK)
                     b.set_piece_at(chess.square(x, y), cpiece)

                  if name == "white-rook":
                     cpiece = chess.Piece(chess.ROOK, chess.WHITE)
                     b.set_piece_at(chess.square(x, y), cpiece)
                  if name == "white-queen":
                     cpiece = chess.Piece(chess.QUEEN, chess.WHITE)
                     b.set_piece_at(chess.square(x, y), cpiece)
                  if name == "white-bishop":
                     cpiece = chess.Piece(chess.BISHOP, chess.WHITE)
                     b.set_piece_at(chess.square(x, y), cpiece)
                  if name == "white-knight":
                     cpiece = chess.Piece(chess.KNIGHT, chess.WHITE)
                     b.set_piece_at(chess.square(x, y), cpiece)
                  if name == "white-pawn":
                     cpiece = chess.Piece(chess.PAWN, chess.WHITE)
                     b.set_piece_at(chess.square(x, y), cpiece)
                  if name == "white-king":
                     cpiece = chess.Piece(chess.KING, chess.WHITE)
                     b.set_piece_at(chess.square(x, y), cpiece)
      global board
      print("imgay")
      board = b

def generate():
   # grab global references to the lock variable
   global lock
   # initialize the video stream
   global vc
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
      # await classify(frame[:, :, ::-1])
      
      classify(frame)
      print("Hi")
      yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
   # release the camera
   vc.release()

app.run()