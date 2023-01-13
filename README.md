# Live-Chess-Engine

![ezgif com-gif-maker](https://user-images.githubusercontent.com/62505788/209054224-ceee1ca0-63a1-488c-a52b-e625ea1c9e7b.gif)

In order to suggest the next best move, we should first know the current position on the chessboard. Using a live video feed, we send frames to the backend, extract the chess board from the image, divide it into 8x8 cells to detect the chessboard grid. For piece detection, we labelled some images and initially used a fine tune pretrained YOLOv5 from object detection api, but changed to Detectron2. We then find the bboxes of each piece that corresponds to the square coordinates and show the position of each piece in the board to the frontend to disaplay as a virtual iamge. We are curerntly using Detectron2 as our CNN and stockfish engine as our chess engine. 

Dataset: https://public.roboflow.com/object-detection/chess-full

## How to use

```shell
git clone https://github.com/leonwangg1/Live-Chess-Engine
flask run
cd frontend
npm start
```
## Issues

- [ ] Poor model accuray
- [ ] Asynchronous implementation
- [x] ~~Stockfish engine not working~~
- [x] ~~Board transformation doesn't detect all squares (maybe try change add padding parameters) - avg (42-list index out of range)~~
- [x] ~~Frame keeps rotating for some reason (detecting other lines?)~~

## Approach

Our approach follows this process:

![image](https://user-images.githubusercontent.com/62505788/167887379-b2e36bbd-80bc-469d-a598-6cd64a6bafae.png)
