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


  Webcam is also similar to video cam just replace it with video location with the webcam number





