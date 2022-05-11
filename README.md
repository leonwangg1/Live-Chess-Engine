# Live-Chess-Engine

In order to suggest the next best move, we should first know the current position on the chessboard. Using a live video feed, we send frames to the backend, extract the chess board from the image, divide it into 8x8 cells, and then send FEN to show the position of each piece in the board to the frontend. We are curerntly using YOLOv5 as our CNN and stockfish engine as our chess engine. 

Dataset: https://public.roboflow.com/object-detection/chess-full

Our approach follows this process:

![image](https://user-images.githubusercontent.com/62505788/167887379-b2e36bbd-80bc-469d-a598-6cd64a6bafae.png)

