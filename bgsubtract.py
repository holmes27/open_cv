import numpy as np
import cv2 as cv

cap=cv.VideoCapture("vtest.avi")
kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
#fgbg=cv.bgsegm.createBackgroundSubtractorMOG() # if error occurs    *****  pip install opencv-contrib-python

#fgbg=cv.createBackgroundSubtractorMOG2(detectShadows= True)# detect shadows

fgbg=cv.bgsegm.createBackgroundSubtractorGMG()

#fgbg=cv.createBackgroundSubtractorKNN()

while(True):
    ret,frame=cap.read()
    if frame is None:
        break
    fgmask=fgbg.apply(frame)
    fgmask=cv.morphologyEx(fgmask,cv.MORPH_OPEN,kernel) # for gmg
    cv.imshow("frame",frame)
    cv.imshow("fg mask",fgmask)

    keyboard=cv.waitKey(30)
    if keyboard=='q' or keyboard==27:
        break

cap.release()
cv.destroyAllWindows()

