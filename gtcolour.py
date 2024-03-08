import numpy as np
import cv2

def get_color(color):

    c=np.uint8([[color]])

    hsvc=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    lowerLimit=hsvc[0][0][0] - 10,100,100
    upperLimit=hsvc[0][0][0] +10,255,255

    lowerLimit=np.array(lowerLimit,dtype=np.uint8)
    upperLimit=np.array(upperLimit,dtype=np.uint8)

    return lowerLimit,upperLimit
