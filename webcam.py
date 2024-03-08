import cv2
import os

webcam=cv2.VideoCapture(0)

while True:
    ret,frames=webcam.read()

    if ret:
        cv2.imshow('web',frames)
        if cv2.waitKey(40) & 0xFF==ord('u'):
            break

webcam.release()
cv2.destroyAllWindows()