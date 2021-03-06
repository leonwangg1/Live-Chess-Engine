from flask import Markup, Flask, render_template, Response, url_for
import threading
import chesspiecedetection
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
import boardextraction
import cv2

app = Flask(__name__)
cfg = chesspiecedetection.load_model()
vc = cv2.VideoCapture(0)
lock = threading.Lock()
board = chess.Board()

@app.route('/')
def main():
    return render_template("test.html")

@app.route('/board')
def board_feed():
    global board
    global cfg
    global cv
    return Response(boardextraction.main(cfg), mimetype = "multipart/x-mixed-replace; boundary=frame")


@app.route('/stream',methods = ['GET'])
def stream():
    return Response(chesspiecedetection.video_prediction(cfg), mimetype = "multipart/x-mixed-replace; boundary=frame")

