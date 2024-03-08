import os
import cv2
import numpy as np

img=cv2.imread(os.path.join('.','images.jpg'))

img2=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
ret,img3=cv2.threshold(img2,80,230,cv2.THRESH_BINARY)

asd=cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,22)

imp_edg=cv2.dilate(asd,np.ones((3,3),dtype=np.int8))
imp_edg1=cv2.erode(asd,np.ones((3,3),dtype=np.int8))

# cv2.imshow('img2',asd)
# cv2.imshow('img3',img3)
# cv2.imshow('img',imp_edg)
cv2.imshow('img',imp_edg1)
cv2.waitKey(0)