import cv2 as cv
import numpy as np

img=cv.imread("sudoku.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges=cv.Canny(gray,50,150,apertureSize=3)

cv.imshow("edge",edges)
lines=cv.HoughLines(edges,1,np.pi/180,200)# 1 is the rho distance from 0,0 and thetha is in radians

for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho
    #x1 stores the rounded off value of (r*cos(theta)-1000*sin(theta))
    x1=int(x0+1000*(-b))
    #y1 stores the rounded off value of (r*sine(theta)+1000*cos(theta))
    y1=int(y0+1000*(a))
    #x2 stores the rounded off value of(r*cos(theta)+1000*sine(theta))
    x2=int(x0-1000*(-b))
    #y2 stores the rounded off value of (r*sine(theta)-1000*cos(theta))
    y2=int(y0-1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)



cv.imshow("image",img)

cv.waitKey(0)
cv.destroyAllWindows()