from flask import Markup, Flask, render_template, Response, url_for
import threading
import chesspiecedetection

app = Flask(__name__)

lock = threading.Lock()

@app.route('/')
def main():
    return render_template("test.html")

app.run()

@app.route('/stream',methods = ['GET'])
def stream():
   return Response(chesspiecedetection.main(), mimetype = "multipart/x-mixed-replace; boundary=frame")
