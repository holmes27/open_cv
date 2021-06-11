import numpy as np
import cv2 as cv

img=cv.imread("chessboard.png")
cv.imshow("image",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray=np.float32(gray)
dst=cv.cornerHarris(gray,2,3,0.04)# 2 is the block size ,3 is for sobel(aperture parameter),0.04 is for harris free detector parameter

dst=cv.dilate(dst,None)# for better results
img[dst>0.01*dst.max()]=[0,0,255]# max change in intensity is the corner

cv.imshow("image with corners",img)

if cv.waitKey(0) & 0xff==27:
    cv.destroyAllWindows()

