import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img [:]=100,230,150

cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(200,100,255),3)
cv2.rectangle(img,(0,0),(250,350),(50,100,255))
cv2.circle(img,(400,50),30,(100,100,200),5)
cv2.putText(img," Hello !",(200,250),cv2.FONT_ITALIC,1,(0,150,0))

cv2.imshow("Image", img)

cv2.waitKey(0)