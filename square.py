import cv2
import numpy as np

class Square:
  """
  Create a representation object of a individual chess board square

  **Coordinates**
  
  (x1, y1)
      •-------+
      |  IMG  |
      +-------•
            (x2, y2)
  """

  x1: int
  y1: int
  x2: int
  y2: int
  isEmpty: bool=True
#   piece: Piece=None

  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
