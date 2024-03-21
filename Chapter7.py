import cv2
import numpy as np
def empty(a):
    pass

img=cv2.imread('lb.jpg')
cv2.namedWindow('trackbar')
cv2.resizeWindow('trackbar',640,240)
cv2.createTrackbar('Hue min','trackbar',0,179,empty)
cv2.createTrackbar('Hue max','trackbar',0,179,empty)
cv2.createTrackbar('sat min','trackbar',0,255,empty)
cv2.createTrackbar('sat max','trackbar',0,255,empty)
cv2.createTrackbar('val min','trackbar',0,255,empty)
cv2.createTrackbar('val max','trackbar',0,255,empty)
while True:
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue min","trackbar")
    h_max=cv2.getTrackbarPos("Hue max","trackbar")
    sat_min = cv2.getTrackbarPos("sat min", "trackbar")
    sat_max = cv2.getTrackbarPos("sat max", "trackbar")
    val_min = cv2.getTrackbarPos("val min", "trackbar")
    val_max = cv2.getTrackbarPos("val max", "trackbar")
    lower=np.array([h_min,sat_min,val_min])
    upper=np.array([h_max,sat_max,val_max])
    mask=cv2.inRange(imghsv,lower,upper)
    imgresult=cv2.bitwise_and(img,img,mask=mask)



    cv2.imshow('img',img)
    cv2.imshow('imgHSV',imghsv)
    cv2.imshow('mask', imgresult)
    cv2.waitKey(1)
    # WE ARE CREATINGA TRACKBAR
