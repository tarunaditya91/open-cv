# open-cv
![image](https://github.com/tarunaditya91/open-cv/assets/113850656/d35e3420-b364-4c0d-9e3d-21b2a7dc9e0e)
# Drawing
![image](https://github.com/tarunaditya91/open-cv/assets/113850656/58425e38-0869-4c47-8ca4-6dd6858c1616)
# contours
![image](https://github.com/tarunaditya91/open-cv/assets/113850656/ae8eb0d0-aa8e-49cc-8ffb-d02a35808c96)
# colorspaces
![image](https://github.com/tarunaditya91/open-cv/assets/113850656/1b3da0d1-bb8a-4a63-8cd9-42c2c920db77)
# blurring
![image](https://github.com/tarunaditya91/open-cv/assets/113850656/d7bb3b87-9865-41ed-92f6-ee261eb4433e)
# resizing
# crop

# Chapter 1 read IMAGE-VIDEO-WEBCAM

IMAGE

to read an image first we have to import cv2 package which has a function imread that helps us to read an image then you have to place the image

to show the image you have to use the function imshow() this function has two attributes
1-> The first one is the name of the image
2-> One is the image variable

to delay the image time we have to use waitkey() function if we add 0 it i infinitely if we add 1 one millisecond delay


VIDEO

now first we have to import cv2 again then we use function VideoCapture()


then we have to read it frame by frame

cv2.imshow("img",img)
cv2.waitKey(0)

img2=cv2.VideoCapture('sample.mp4')

while True:
    img,suu=img2.read()
    cv2.imshow('v',suu)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


  A webcam is also similar to a video cam just replace it with video location with the webcam number and we can also re-size it using this 

  img2.set(3,340)this is 3->width,340->width size
img2.set(4,380)this  is 4->height,380->height size


we can also change the brightness by using 

img2.set(10,100) 10->is id for brightness 

# Basic Functions


  Now first thing we will do that to convert it into gray scale

  first you have to import cv2

  and use a function cvtColor() function  .for creating a image we use rgb but in cv2 it is bgr to covert it into gray we use the following code 

  import cv2

img=cv2.imread('images.jpg')

imgGray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
imgblur=cv2.GaussianBlur(imgGray,(7,7),0)

cv2.imshow('imgGray',imgGray)
cv2.imshow('imgblur',imgblur)
cv2.waitKey(0)

![image](https://github.com/tarunaditya91/open-cv/assets/113850656/51d19746-2856-4245-8710-f4f93fb93a7d)


Next we work on canny edge dettection 

imgcanny=cv2.Canny(img,100,100)

![image](https://github.com/tarunaditya91/open-cv/assets/113850656/ebf5fa7e-174d-46ab-b570-31a79dbff8f7)

to reduse the edges change the threshold values

imgcanny=cv2.Canny(img,150,250)
you can seethe diffrence
![image](https://github.com/tarunaditya91/open-cv/assets/113850656/61057c22-dead-4d99-9079-600926d43f28)

Dilation -> some times the edges are not connected we can increase the thickness useing dilation

KERNAL IS NOTING BUT A MATRIX VALUE WHICH WE HAV TO EEFINE MATRIX VALUE AND SIZE FOR THIS WE NEED THE MATRIX VALUE AS ONE 


For doing this we need numpy which we have to import it 


np.uint8 refers to an 8-bit unsigned integer data type in the NumPy library in Python. It stands for "NumPy unsigned integer 8-bit". This data type can represent integers ranging from 0 to 255. It is commonly used for storing image data, especially in grayscale images, where pixel values typically range from 0 (black) to 255 (white).

Now we have to create s Kernal =np.onse((5,5),np.unit8)

image after applying Dialation
![image](https://github.com/tarunaditya91/open-cv/assets/113850656/27744c94-970b-4611-a832-bb8592468256)


The next function is Erode

Erode is the reverse process of Dialation 

imgEroded=cv2.erode(imgDialation,kernal,iterations=1)

![image](https://github.com/tarunaditya91/open-cv/assets/113850656/165999c8-48f3-4aed-87fd-eaa296ecada8)

# chapter 3
# Resizeing_and_cropping
opencv convention 

imgresize=cv2.resize(img(200,300)) first width and then height

![image](https://github.com/tarunaditya91/open-cv/assets/113850656/cbc9c2bd-d666-4ff3-9b60-3443d9427b08)

in open cv fuction width will come first then height

for croping we wont need cv2 we cann do it useing matrix 
![image](https://github.com/tarunaditya91/open-cv/assets/113850656/8eb945f9-de02-49b1-8c0a-e1a2bb461590)

imgcrop=img[0:300,50:100]
# Chapter 4
SHAPES_AND_TEXT

cv2.line(img,(0,0),(300,300),(0,255,0),3) for drawing a line 


![image](https://github.com/tarunaditya91/open-cv/assets/113850656/cad4d274-d5a7-4326-add6-3d4ddb1f4df3)

cv2.rectangle(imgr,(0,0),(200,200),(0,0,255),3) for drawing rectangle


![image](https://github.com/tarunaditya91/open-cv/assets/113850656/452a8719-dbdb-47a9-8b5e-a7aaaa6f77ca)

cv2.rectangle(imgr,(0,0),(200,200),(0,0,255),cv2.FILLED)

![image](https://github.com/tarunaditya91/open-cv/assets/113850656/4ecf0026-a7f2-4a49-8945-0c0c33ea9b5d)

cv2.circle(imgr,(150,150),8,(255,0,0),cv2.FILLED)


![image](https://github.com/tarunaditya91/open-cv/assets/113850656/bfd9ba2e-402e-4d22-962f-56f1b719d88e)

cv2.putText(imgr,"opencv text",(200,100),cv2.FONT_HERSHEY_PLAIN,1,(0,150,0),1)

![image](https://github.com/tarunaditya91/open-cv/assets/113850656/3179cdd3-7733-4015-9df7-5e886dfc7584)


# chapter 5
WARP_PERSPECTIVE

![image](https://github.com/tarunaditya91/open-cv/assets/113850656/bfa5f40b-9017-4d99-863d-70d5d104a5b5)

# cHAPTER 6 
JOINING_IMAGES

import numpy as np
import cv2

img=cv2.imread('images.jpg')

imghor=np.hstack((img,img))
imgver=np.vstack((img,img))

cv2.imshow("horizontal",imghor)
cv2.imshow("vertical",imgver)
cv2.waitKey(0)

![image](https://github.com/tarunaditya91/open-cv/assets/113850656/1de41c09-27df-475c-b4e4-f7df567218bd)


![image](https://github.com/tarunaditya91/open-cv/assets/113850656/42c5e5fc-421a-4c72-969e-971ab880f849)

#Chapter 7
COLOR_DETECTION

imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

![image](https://github.com/tarunaditya91/open-cv/assets/113850656/e088070b-9c10-4a6c-82a6-2670290c1054)

We are creating a trackbar

first, we have to create a named window then we have to resize the window  then from cv2 use the function createTrackbar first enter the value you want then the window name starting and ending, then a function


![image](https://github.com/tarunaditya91/open-cv/assets/113850656/e94886fb-5380-478b-b060-01246e0145af)






![image](https://github.com/tarunaditya91/open-cv/assets/113850656/2da25e52-a536-4c33-8ea7-f78339eb1ab6)


![image](https://github.com/tarunaditya91/open-cv/assets/113850656/0e9ec8e8-94d9-4492-ab06-e37d4be20713)


# Chapter 8
 CONTOURS/SHAPE DETECTION


 ![image](https://github.com/tarunaditya91/open-cv/assets/113850656/65e89f60-209d-40b5-99d5-e0b4ad4b299c)












