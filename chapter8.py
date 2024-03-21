import cv2
import numpy as np

def getcontors(img):
    contors,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contors:
        area=cv2.contourArea(cnt)
        print(area)

        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri=cv2.arcLength(cnt,True)
            # print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objcor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)

            if objcor==3: objectType="tri"
            else:objectType="ni"
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)




img=cv2.imread('shapes.jpg')
print(img.shape)

imgresize=cv2.resize(img,(500,500))
imgContour=imgresize.copy()

imgGray=cv2.cvtColor(imgresize,cv2.COLOR_BGR2GRAY)
imgCanny=cv2.Canny(imgGray,50,50)
getcontors(imgCanny)

cv2.imshow('original',imgresize)
cv2.imshow('IMGgRAY',imgGray)
cv2.imshow('imgCanny',imgCanny)
cv2.imshow('imgContor',imgContour)

cv2.waitKey(0)