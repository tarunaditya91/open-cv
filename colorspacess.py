import os

import cv2

img=cv2.imread(os.path.join('.','images.jpg'))

colr_space=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
colr_space1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
colr_space11=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


cv2.imshow('colr_space',colr_space)
cv2.imshow('colr_space1',colr_space1)
cv2.imshow('colr_space11',colr_space11)
cv2.waitKey(0)