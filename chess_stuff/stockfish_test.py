import chess
import chess.engine
import chess.svg
import sys

# stockfish = Stockfish(path="./stockfish testing/stockfish_15_x64_avx2")
board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("./stockfish_15_x64_avx2")

# info = engine.play(board, chess.engine.Limit(time=1))
# board.push(info.move)

#svgWidget.load(chess.svg.board(board).encode("UTF-8"))
# engine.quit()

# sys.exit(app.exec_())
