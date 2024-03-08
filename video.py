import cv2

video=cv2.VideoCapture('pexels-tima-miroshnichenko-5955336 (2160p).mp4')


ret=True

while ret:
    ret,frames=video.read()

    if ret:
        cv2.imshow('frames',frames)
        if cv2.waitKey(40) & 0xFF==ord('q'):
          break
        

video.release()
cv2.destroyAllWindows()