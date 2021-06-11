import cv2
img=cv2.imread('lena.jpg',-1)
print(img)
cv2.imshow('image',img)
k=cv2.waitKey(5000) &0xFF #0 instead of 5000- wont disappear the other argument is for 64 bit
if k==27:# escape key is pressed
    cv2.destroyAllWindows()#destroyWindow()- one window destruction
elif k==ord('s'):#s key pressed
    cv2.imwrite("lena_copy.png",img)
    cv2.destroyAllWindows()