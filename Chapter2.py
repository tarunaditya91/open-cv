import cv2
import numpy as np

img=cv2.imread('images.jpg')

imgGray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
imgblur=cv2.GaussianBlur(imgGray,(7,7),0)

kernal=np.ones((5,5),np.uint8)

imgcanny=cv2.Canny(img,150,250)
imgDialation=cv2.dilate(imgcanny,kernal,iterations=1)

imgEroded=cv2.erode(imgDialation,kernal,iterations=1)

cv2.imshow('imgGray',imgGray)
cv2.imshow('imgblur',imgblur)
cv2.imshow('imgCanny',imgcanny)
cv2.imshow('imgDialation',imgDialation)
cv2.imshow('imgEroded',imgEroded)
cv2.waitKey(0)