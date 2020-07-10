import cv2

#load image
img = cv2.imread("res/lena.png")
print(img.shape)
imgResize = cv2.resize(img,(300,300))

imgCrop = img[0:200,200:400]

cv2.imshow("output", img)
cv2.imshow("resize", imgResize)
cv2.imshow("croped", imgCrop)
cv2.waitKey(0)