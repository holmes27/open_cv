import cv2 as cv
import numpy as np

img=cv.imread('sudoku.png',0)

_,th1=cv.threshold(img,50,255,cv.THRESH_BINARY)
th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
# max pixel can be 255 ,11= block size(neighbourhood area),2 is c value
th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

cv.imshow("Image",img)
cv.imshow("th1",th1)
cv.imshow("th2",th2)
cv.imshow("th3",th3)


cv.waitKey(0)
cv.destroyAllWindows()