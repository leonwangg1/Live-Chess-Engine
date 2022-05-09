import cv2
import os
file_dir = "./chess_stuff/"
files = os.listdir(file_dir)
img_files = list(filter(lambda x: '.jpg' in x, files))
# image = open("./chess_stuff/0b47311f426ff926578c9d738d683e76_jpg.rf.40183eae584a653181bbd795ba3c353f.jpg")

# image = cv2.imread("./chess_stuff/0b47311f426ff926578c9d738d683e76_jpg.rf.40183eae584a653181bbd795ba3c353f.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img = cv2.imread("./chess_stuff/0b47311f426ff926578c9d738d683e76_jpg.rf.40183eae584a653181bbd795ba3c353f.jpg",0)
blur = cv2.GaussianBlur(img,(5,5),0)
_, img_binary = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("gay", img_binary)
cv2.waitKey(1000)

# for i in img_files:
    # image = cv2.imread(file_dir + i)
    # # print(cv2.checkChessboard(image, (7, 7)))
    # # cv2.chess
    # corners = cv2.findChessboardCorners(image, (7, 7))

    # cv2.imshow("image", cv2.drawChessboardCorners(image, (7,7), corners[1], corners[0]))
    # cv2.waitKey(300)
    
    
    