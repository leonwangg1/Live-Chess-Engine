# Live-Chess-Engine

In order to suggest the next best move, we should first know the current position on the chessboard. Using a live video feed, we send frames to the backend, extract the chess board from the image, divide it into 8x8 cells to detect the chessboard grid. For piece detection, we labelled some images and initially used a fine tune pretrained YOLOv5 from object detection api, but changed to Detectron2. We then find the bboxes of each piece that corresponds to the square coordinates and show the position of each piece in the board to the frontend to disaplay as a virtual iamge. We are curerntly using Detectron2 as our CNN and stockfish engine as our chess engine. 

Dataset: https://public.roboflow.com/object-detection/chess-full

## Files

- w.i.p

## How to use

```shell
git clone https://github.com/leonwangg1/Live-Chess-Engine
flask run
cd frontend
npm start
```
## Challenges

- Model bad accuracy in top down
- Asynchronous implementation

## Approach

Our approach follows this process:

![image](https://user-images.githubusercontent.com/62505788/167887379-b2e36bbd-80bc-469d-a598-6cd64a6bafae.png)

Issues
- model accuracy kinda shit
- <strike>stockfish engine not working<strike>
-  <strike>board transformation doesn't detect all squares (maybe try change add padding parameters) - avg (42-list index out of range) <strike>
-  <strike>frame keeps rotating for some reason (due to detecting other lines)<strike>
