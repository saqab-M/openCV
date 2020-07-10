import cv2
import numpy as np

img = cv2.imread("res/cards.jpg")

width, height = 250 ,350
points = np.float32([[111,219],[287,188],[154,482],[352,440]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(points,points2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("output", img)
cv2.imshow("warp", imgOutput)

cv2.waitKey(0)