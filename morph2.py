import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('opencv\samples\data\pic1.png',cv.IMREAD_GRAYSCALE) # already a binary image, don't apply mask
kernal=np.ones((5,5),np.uint8)

dilation=cv.dilate(img,kernal,iterations=2)
erosion=cv.erode(img,kernal,iterations=1)
opening=cv.morphologyEx(img,cv.MORPH_OPEN,kernal)# erosion followed by dilation
closing=cv.morphologyEx(img,cv.MORPH_CLOSE,kernal)# dilation followed by erosion
mg=cv.morphologyEx(img,cv.MORPH_GRADIENT,kernal)# difference between dilation and erosion
th=cv.morphologyEx(img,cv.MORPH_TOPHAT,kernal)#difference between opeing and image

titles=['image','dilation','erosion','opening','closing','mg','th']
images=[img,dilation,erosion,opening,closing,mg,th]

for i in range(7):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()