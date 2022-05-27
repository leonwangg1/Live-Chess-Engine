# load config
import json
with open('roboflow_config.json') as f:
    config = json.load(f)

    ROBOFLOW_API_KEY = config["ROBOFLOW_API_KEY"]
    ROBOFLOW_MODEL = config["ROBOFLOW_MODEL"]
    ROBOFLOW_SIZE = config["ROBOFLOW_SIZE"]

    FRAMERATE = config["FRAMERATE"]
    BUFFER = config["BUFFER"]

import cv2
import base64
import numpy as np
import requests
import time
from PIL import Image

# Construct the Roboflow Infer URL
# (if running locally replace https://detect.roboflow.com/ with eg http://127.0.0.1:9001/)
upload_url = "".join([
    "https://detect.roboflow.com/",
    ROBOFLOW_MODEL,
    "?api_key=",
    ROBOFLOW_API_KEY,
    "&format=image",
    "&stroke=5"
])

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Infer via the Roboflow Infer API and return the result
def infer():
    # check camera is open
    if video.isOpened():
        # Get the current image from the webcam
        ret, img = video.read()
        if img is not None:
            # Resize (while maintaining the aspect ratio) to improve speed and save bandwidth
            height, width, channels = img.shape
            scale = ROBOFLOW_SIZE / max(height, width)
            img = cv2.resize(img, (round(scale * width), round(scale * height)))
            
            # Encode image to base64 string
            retval, buffer = cv2.imencode('.jpg', img)
            img_str = base64.b64encode(buffer)

            # Get prediction from Roboflow Infer API
            resp = requests.post(upload_url, data=img_str, headers={
                "Content-Type": "application/x-www-form-urlencoded"
            }, stream=True).raw

            # Parse result image
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            cv2.imshow('image', image)
            cv2.waitKey(1)
            return image
    else:
        ret = False

# Main loop; infers sequentially until you press "q"
while 1:
    # On "q" keypress, exit
    if(cv2.waitKey(1) == ord('q')):
        break

    # Synchronously get a prediction from the Roboflow Infer API
    image = infer()
    # And display the inference results
    # if image is not None:
    #     print('showing frame')
    #     cv2.imshow('image', image)
    #     cv2.waitKey(1)
    # else:
    #     print('fail')
