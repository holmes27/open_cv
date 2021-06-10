import numpy as np
import cv2

#events= [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(255,0,0),-1)
        points.append((x,y))
        if len(points)>= 2:
            cv2.line(img,points[-1],points[-2],(55,0,0),2)
        cv2.imshow('image',img)
    
    


img=np.zeros([512,512,3],np.uint8)# FOR BLACK IMAGE
points=[]
#img=cv2.imread('lena.jpg')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)# frame window name should be same everywhere

cv2.waitKey(0)
cv2.destroyAllWindows()
