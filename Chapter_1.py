import cv2
print("opencv imported")

#load image
img = cv2.imread("res/lena.png")
cv2.imshow("output", img)
cv2.waitKey(0)

#load video

#vid = cv2.VideoCapture("res/test_video.mp4")
vid = cv2.VideoCapture(0)
vid.set(3,640) #width
vid.set(4,480) #hight
vid.set(10,100) #brightness
while True:
    success, imgv = vid.read()
    cv2.imshow("video",imgv)
    if cv2.waitKey(1) & 0xff == ord("x"):
        break