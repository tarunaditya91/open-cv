import cv2
import os


imgg=cv2.imread('images.jpg')
print(type(imgg))
# image is nothing but numpyarray

print(imgg.shape)
# output
#(168, 300, 3)height,weight,channel

# img_path=os.path.join('.','OpenCv','images.jpg')
# img=cv2.imread(img_path)
# print(type(img))

# cv2.imwrite(os.path.join('.','OPENCV','images_1.jpg'),img)
cv2.imshow('image',imgg)
cv2.waitKey(0)