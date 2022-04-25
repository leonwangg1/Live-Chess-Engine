from flask import Markup, Flask, render_template
from chess_stuff import stockfish_test
import chess.svg

app = Flask(__name__)

@app.route('/')
def main():
    svg = chess.svg.board(stockfish_test.board)
    # return render_template("test.html", svg=Markup(svg))
    return Markup(svg)