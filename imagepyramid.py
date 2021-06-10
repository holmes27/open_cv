import cv2 as cv
import numpy as np

img=cv.imread("lena.jpg")
lr1=cv.pyrDown(img)
lr2=cv.pyrDown(lr1)
hr1=cv.pyrUp(lr2)

cv.imshow("Original image",img)
cv.imshow("pyr down 1 image",lr1)
cv.imshow("pyr down 2 image",lr2)
cv.imshow("Pyr up image",hr1)

cv.waitKey(0)
cv.destroyAllWindows()