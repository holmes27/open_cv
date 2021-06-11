import cv2
import numpy as np

#img=cv2.imread('lena.jpg',1)
img=np.zeros([512,512,3],np.uint8)# creating black image using np zeros method -[ height,width,3] , data type
 
img=cv2.line(img,(0,0),(255,255),(147,44,94),6) # image,start, end,(b,g,r) ,thickness
img=cv2.arrowedLine(img,(255,0),(255,255),(255,0,94),6)
img=cv2.rectangle(img,(0,0),(510,510),(147,0,0),20)# instead of 20 i.e. thickness if u give -1 it will fill the rectangle with given color
img=cv2.circle(img,(445,255),60,(0,252,0),-1)# centre,radius
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'Hello',(10,500),font,4,(10,255,255),10,cv2.LINE_AA)#image,text,start,font face,font size,color, thickness,type of line

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()