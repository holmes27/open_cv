import cv2 as cv
import numpy as np

img=cv.imread("lena.jpg")
layer=img.copy()
#gaussian 
gp=[layer]

for i in range(6):
    layer=cv.pyrDown(layer)
    gp.append(layer)
    #cv.imshow(str(i),layer)

layer=gp[5]
cv.imshow("Upper level gaussian pyramid",layer)
#laplacian
lp=[layer]
for i in range(5,0,-1):
    gaussian_extended=cv.pyrUp(gp[i])
    laplacian=cv.subtract(gp[i-1],gaussian_extended)
    cv.imshow(str(i),laplacian)
    
cv.imshow("Original image",img)

cv.waitKey(0)
cv.destroyAllWindows()