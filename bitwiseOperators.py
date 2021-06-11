import cv2
import numpy as np

img=np.zeros((288,512,3),np.uint8)
img=cv2.rectangle(img,(200,0),(300,100),(255,255,255),-1)
img2=cv2.imread('image_1.png')

bitAnd=cv2.bitwise_and(img2,img)
bitOr=cv2.bitwise_or(img2,img)
bitXor=cv2.bitwise_xor(img2,img)
bitnot=cv2.bitwise_not(img2)
bitnot1=cv2.bitwise_not(img)

cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.imshow('bitAnd',bitAnd)
cv2.imshow('bitOr',bitOr)
cv2.imshow('bitXor',bitXor)
cv2.imshow('bitnot',bitnot)
cv2.imshow('bitnot1',bitnot1)

cv2.waitKey(0)
cv2.destroyAllWindows()