import os 

import cv2

img=cv2.imread(os.path.join('.','tarun_img.jpg'))


#line

img_line=cv2.line(img,(100,150),(300,450),(0,250,0),3)
# rectangle
img_line2=cv2.rectangle(img,(100,150),(300,450),(0,0,250),3)
#circl
img_line3=cv2.circle(img,(500,500),150,(255,0,0),3)

#text

img_line4=cv2.putText(img,'kks',(345,454),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,0),2)

cv2.imshow('cop_img',img_line4)
cv2.waitKey(0)