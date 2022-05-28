# install dependencies: (use https://pytorch.org/get-started/locally/ based on your cuda version installed)
# pip install -U torch==1.5 torchvision==0.6 -f https://download.pytorch.org/whl/cu101/torch_stable.html 
# pip install cython pyyaml==5.1
# git clone https://github.com/facebookresearch/detectron2.git
# pip install -e detectron2

import cv2
import torch
print(torch.__version__, torch.cuda.is_available())
import os
import time
from scipy import ndimage
import detectron2
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.data.catalog import DatasetCatalog
from detectron2.utils.visualizer import ColorMode
from detectron2.data.datasets import register_coco_instances

# Load model
def load_model():
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file('COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml'))
    cfg.DATASETS.TRAIN = ("my_dataset_train",)
    cfg.DATASETS.TEST = ("my_dataset_val",)
    cfg.MODEL.WEIGHTS = 'models\model_final.pth' # Set path model .pth
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 14
    test_metadata = MetadataCatalog.get("my_dataset_test")
    key = "instances"
    return cfg

def main():
    # Register dataset for detectron2
    register_coco_instances("my_dataset_train", {}, "dataset/train/_annotations.coco.json", "dataset/train")
    register_coco_instances("my_dataset_val", {}, "dataset/valid/_annotations.coco.json", "dataset/valid")
    my_dataset_train_metadata = MetadataCatalog.get("my_dataset_train")
    dataset_dicts = DatasetCatalog.get("my_dataset_train")

    cfg = load_model()
    test_metadata = MetadataCatalog.get("my_dataset_test")
    key = "instances"

    predictor = DefaultPredictor(cfg)
    vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        # check camera is open
        if vid.isOpened():
                ret, frame = vid.read()
                outputs = predictor(frame)
                v = Visualizer(frame[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=0.5, instance_mode=ColorMode.SEGMENTATION)
                out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
                (flag, encodedImage) = cv2.imencode(".jpg", out.get_image()[:, :, ::-1])
                yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
                # cv2.imshow("frame", out.get_image()[:, :, ::-1])
                # cv2.waitKey(1)
        else:
            ret = False

