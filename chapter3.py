import cv2
import numpy as np

img=cv2.imread('images.jpg')

print(img.shape)
imgresize=cv2.resize(img,(200,100))
print(imgresize  .shape)

imgcrop=img[0:300,50:100]
cv2.imshow('img',img)
cv2.imshow('imgresize',imgresize)
cv2.imshow('imgcrop',imgcrop)

cv2.waitKey(0)