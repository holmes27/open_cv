import cv2 as cv
face_cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")

cap=cv.VideoCapture("output.mp4")

while(cap.isOpened()):
    _,img=cap.read()
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)


    cv.imshow("img",img)
    if cv.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()