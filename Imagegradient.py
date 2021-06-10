import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('messi5.jpg',cv.IMREAD_GRAYSCALE)
lap=cv.Laplacian(img,cv.CV_64F,ksize=3)#kernel size=3
lap=np.uint8(np.absolute(lap))
sobelX=cv.Sobel(img,cv.CV_64F,1,0)# 1,0 FOR X
sobelY=cv.Sobel(img,cv.CV_64F,0,1)#0,1 FOR Y

sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

sobelCombined=cv.bitwise_or(sobelX,sobelY)

titles=['image','laplacian','sobelX','sobelY','sobelCombined']
images=[img,lap,sobelX,sobelY,sobelCombined]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])



plt.show()