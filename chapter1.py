import cv2

# img=cv2.imread("images.jpg")
# print(img.shape)
#
# cv2.imshow("img",img)
# cv2.waitKey(0)

img2=cv2.VideoCapture(0)

img2.set(3,340)
img2.set(4,380)

img2.set(10,100)

while True:
    img,suu=img2.read()
    cv2.imshow('v',suu)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break