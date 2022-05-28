from flask import Markup, Flask, render_template, Response, url_for
import threading
import chesspiecedetection
import perspective
import chess
import chess.engine
import chess.svg
import detectron2
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.data.catalog import DatasetCatalog
from detectron2.utils.visualizer import ColorMode
from detectron2.data.datasets import register_coco_instances
import time
import cv2

app = Flask(__name__)
cfg = chesspiecedetection.load_model()
vc = cv2.VideoCapture(0)
lock = threading.Lock()
board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("./stockfish_15_x64_avx2")

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
    global engine
    _, frame = vc.read()
    board = classify(frame)
    move = None
    try:
       move = engine.play(board, chess.engine.Limit(time=0.5)).move
    except Exception as e:
       engine = chess.engine.SimpleEngine.popen_uci("./stockfish_15_x64_avx2")
    if move is None:
       svg = chess.svg.board(board, size=400)
    else:
      svg = chess.svg.board(board, size=400, arrows=[chess.svg.Arrow(move.from_square, move.to_square)])
    yield ('--frame\r\n'
                'Content-Type: image/svg+xml\r\n\r\n' + svg + '\r\n')
    # time.sleep(4)

def generate():
   # grab global references to the lock variable
   global lock
   # initialize the video stream
   
   
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
      
      yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
   # release the camera
   vc.release()

@app.route('/stream',methods = ['GET'])
def stream():
    # return Response(chesspiecedetection.main(), mimetype = "multipart/x-mixed-replace; boundary=frame")
    return Response(generate(), mimetype = "multipart/x-mixed-replace; boundary=frame")

def classify(im):
    b = chess.Board(None)
    im = perspective.change_perspective(im)   
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
    
    predictor = DefaultPredictor(cfg)
    outputs = predictor(im)
    prediction_boxes = outputs["instances"].pred_boxes
    metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])
    class_catalog = metadata.thing_classes
    for idx, coordinates in enumerate(prediction_boxes):
        w = (coordinates[0] + coordinates[1])/2
        h = (coordinates[2] + coordinates[3])/2
        for x in range(0, 8):
            for y in range(0, 8):
                xs = boardarray[x][y][0][0]
                xe = boardarray[x][y][0][1]
                ys = boardarray[x][y][1][0]
                ye = boardarray[x][y][1][1]
                if w >= xs and w <= xe and h >= ys and h <= ye:
                    square = chess.square(x, y)
                    class_index = outputs["instances"].pred_classes[idx]
                    name = class_catalog[class_index]
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
    return b
