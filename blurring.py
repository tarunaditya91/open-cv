import os
import cv2

img=cv2.imread(os.path.join('.','images.jpg'))


k_size=7
img_se=cv2.blur(img,(k_size,k_size))
img_se1=cv2.GaussianBlur(img,(k_size,k_size),5)
img_se2=cv2.medianBlur(img,k_size)


cv2.imshow('img_se',img_se)
cv2.imshow('img_se1',img_se1)
cv2.imshow('img_se2',img_se2)
cv2.waitKey(0)