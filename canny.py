import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('messi5.jpg',cv.IMREAD_GRAYSCALE)
canny=cv.Canny(img,100,200)#image,threshold1,threshold2 , lesser noise is there in this method as compared to image gradients

titles=['image','canny']
images=[img,canny]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()