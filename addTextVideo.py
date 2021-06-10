import cv2
import datetime

cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))# each property has a number 3 for example
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(3,1208)#3 for width
#cap.set(4,720)#4 for height 
# if we give 700 as width and 700 as height, the resolution will  be the  available one 640 and 480

#print(cap.get(3))
#print(cap.get(4))

while(cap.isOpened()): # instead of true put **cap.isOpened()** this will tell the frame is correct or not, for 8 it will return false
     ret, frame= cap.read()
     if(ret==True):

        font=cv2.FONT_HERSHEY_SIMPLEX
        text='Width:'+ str(cap.get(3))+'Height:'+str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,50),font,1,(255,255,255),2,cv2.LINE_AA)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1)& 0xFF==ord('q'):
            break
     else:
         break
    
cap.release()

cv2.destroyAllWindows()
