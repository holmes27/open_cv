import cv2 as cv
from matplotlib import pyplot as plt


img=cv.imread('lena.jpg')
# matplotlib rgb opencv bgr format so change color format

img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]),plt.yticks([]) # to hide the x ticks
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()