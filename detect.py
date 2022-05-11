import torch
import cv2
from PIL import Image
import chess
import perspective

b = chess.Board(None)
model = torch.hub.load('yolov5-master', 'custom', path='best.pt', source='local')

im = cv2.imread('IMG_20220511_215025.jpg')
im = perspective.change_perspective(im)
x, y, _ = im.shape
board = []
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
    board.append(row)

results = model(im)
results.show()
print(results.pandas().xyxy[0])
for i in range(0, len(results.pandas().xyxy[0])):
    piece = results.pandas().xyxy[0].iloc[i]
    w = (piece["xmin"] + piece["xmax"])/2
    h = (piece["ymin"] + piece["ymax"])/2
    point = (w, h)
    for x in range(0, 8):
        for y in range(0, 8):
            xs = board[x][y][0][0]
            xe = board[x][y][0][1]
            ys = board[x][y][1][0]
            ye = board[x][y][1][1]
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
                    
print(b.fen())