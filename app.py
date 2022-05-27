from flask import Markup, Flask, render_template, Response, url_for
import cv2
import chess.svg
import chess.engine
import chess
import numpy as np
import requests
# import piecedetection

app = Flask(__name__)

# model = torch.hub.load('yolov5-master', 'custom', path='best.pt', source='local')

@app.route('/')
def main():
    return render_template("test.html")

# @app.route('/stream',methods = ['GET'])
# def stream():
#    return Response(generate(), mimetype = "multipart/x-mixed-replace; boundary=frame")

# def generate():
#     while 1:
#         image = piecedetection.infer()
#         return image
        
app.run()