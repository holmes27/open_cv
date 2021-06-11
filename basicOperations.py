import cv2
import numpy as np

img=cv2.imread('messi5.jpg')
img2=cv2.imread('opencv-logo.png')

print(img.shape)#tuple of rows,columns,channels
print(img.size)#total number of pixels
print(img.dtype)#image datatype

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

#region of interest, copy the ball and paste it 

ball=img[280:340,330:390]#copy # know the coordinates using the previous mouse click event 
img[273:333,140:200]=ball#paste

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

#dst=cv2.add(img,img2)# same size images are added
dst=cv2.addWeighted(img,0.5,img2,0.8,0)# documentation for syntax; 0=gamma here for scalar

cv2.imshow('image',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()