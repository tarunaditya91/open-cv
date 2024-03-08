import cv2
import os
from PIL import Image

from gtcolour import get_color

yellow=[0,255,255]


webcam=cv2.VideoCapture(0)


while True:
    ret,frames=webcam.read()


    hsvImage=cv2.cvtColor(frames,cv2.COLOR_BGR2HSV)

    lowr,upper=get_color(color=yellow)

    mask=cv2.inRange(hsvImage,lowr,upper)

    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    if bbox is not None:
        x1,y1,x2,y2=bbox
        frames=cv2.rectangle(frames,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow('web',frames)
    if cv2.waitKey(1) & 0xFF==ord('u'):
        break



webcam.release()
cv2.destroyAllWindows()