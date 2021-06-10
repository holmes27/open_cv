import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('lena.jpg')
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

kernel=np.ones((5,5),np.float32)/25

dst=cv.filter2D(img,-1,kernel)
blur=cv.blur(img,(5,5))
gblur=cv.GaussianBlur(img,(5,5),0)
median=cv.medianBlur(img,5)#that number should be more than 1 and odd , salt pepper noise
bilateralFilter=cv.bilateralFilter(img,9,75,75)#for edges to be sharper and noise removal (diameter,sigma color,sigma space)

titles=['image','dst','blur','GaussianBlur','medianBlur','Bilateral Filter']
images=[img,dst,blur,gblur,median,bilateralFilter]


for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])



plt.show()