import numpy as np
import cv2 as cv

img=cv.imread("pic1.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners=cv.goodFeaturesToTrack(gray,25,0.01,10)# 25 is max number of corners, 0.01 is minimum quality, 10 is the minimum distance between corners
corners=np.int0(corners)
for i in corners:
    x,y=i.ravel()
    cv.circle(img,(x,y),3,255,-1)


cv.imshow("image with corners",img)

if cv.waitKey(0) & 0xff==27:
    cv.destroyAllWindows()

