import numpy as np
import cv2

img=cv2.imread('images.jpg')

imghor=np.hstack((img,img))
imgver=np.vstack((img,img))

cv2.imshow("horizontal",imghor)
cv2.imshow("vertical",imgver)
cv2.waitKey(0)