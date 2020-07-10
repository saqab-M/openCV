import cv2
import numpy as np

img = cv2.imread("res/lambo.png")
kernal = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img,200,250)
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)
imgEroded = cv2.erode(imgDialation,kernal,iterations=1)

cv2.imshow("output", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dialation", imgDialation)
cv2.imshow("Eroded", imgEroded)

cv2.waitKey(0)

#load video

vid = cv2.VideoCapture(0)
vid.set(3,640) #width
vid.set(4,480) #hight
vid.set(10,100) #brightness
while True:
    success, imgv = vid.read()
    imgv = cv2.Canny(imgv,150,150)
    cv2.imshow("video",imgv)
    if cv2.waitKey(1) & 0xff == ord("x"):
        break