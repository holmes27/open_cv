import cv2 as cv
import numpy as np
img=cv.imread("shapes.jpg")

imgray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)# binary image better for contour

_,thresh=cv.threshold(imgray,240,255,cv.THRESH_BINARY)
contours,_=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx=cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
    cv.drawContours(img,[approx],0,(0,0,0),5)
    x=approx.ravel()[0]
    y=approx.ravel()[1]-10
    if len(approx)==3:
        cv.putText(img,"triangle",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==4:
        x1,y1,w,h=cv.boundingRect(approx)
        aspectRatio=float(w)/h
        print(aspectRatio)
        if aspectRatio>=0.95 and  aspectRatio<=1.05:
            cv.putText(img,"square",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        else:
            cv.putText(img,"rectangle",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==5:
        cv.putText(img,"pentagon",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==10:
        cv.putText(img,"star",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    else:
        cv.putText(img,"Circle",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))


cv.imshow('shapes',img)

cv.waitKey(0)
cv.destroyAllWindows()