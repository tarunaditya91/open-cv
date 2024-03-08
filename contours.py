import os 

import cv2

img=cv2.imread(os.path.join('.','tarun2.webp'))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img_at=cv2.threshold(img_gray,12,255,cv2.THRESH_BINARY_INV)

Contours,hierarchy=cv2.findContours(img_at,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

image_corus=img.copy()

# cv2.drawContours(image_corus, Contours, -1, (0, 255, 0), 2) 

for cn in Contours:
    if cv2.contourArea(cn)>200:
        # cv2.drawContours(img,cn,-1,(0,0,225),2)

        x1,y1,w,h=cv2.boundingRect(cn)

        cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),2)

cv2.imshow('cofp_img',img_at)
cv2.imshow('cofp_img',img)
cv2.waitKey(0)