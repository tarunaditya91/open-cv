import  cv2

import numpy as np
img=np.zeros((512,512,3),np.uint8)

imgr=img[0:300,0:300]
cv2.line(imgr,(0,0),(300,300),(0,255,0),3)
print(imgr.shape)

cv2.rectangle(imgr,(0,0),(200,200),(0,0,255),cv2.FILLED)
cv2.circle(imgr,(150,150),8,(255,0,0),cv2.FILLED)

cv2.putText(imgr,"opencv text",(200,100),cv2.FONT_HERSHEY_PLAIN,1,(0,150,0),1)
cv2.imshow('img',imgr)
cv2.waitKey(0)