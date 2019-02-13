import cv2
import numpy as np
from time import sleep
cap = cv2.VideoCapture(0)
r=0
b=0
g=0
ret, frame = cap.read()
cv2.imshow("frame",frame)
frame2 = frame[180:280,450:550]
cv2.imshow("frame2",frame2)
frame1=cv2.resize(frame2, (400,400))
cv2.imshow("frame1",frame1)
   
   
x=0
y=0
R=[] 
G=[]
B=[] 
for n in range(0,255):
    lower_range = np.array([n, 0, 0])
    upper_range = np.array([n+1, 255, 255])
    mask = cv2.inRange(frame1, lower_range, upper_range)
    contour = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    res=cv2.bitwise_and(frame1,frame1,mask=mask)
    for p in contour:
        cv2.drawContours(frame1, [p], -1, (0,255,0), 3) 
    for c in contour:
       x+=cv2.contourArea(c)
    R.append(x)
    x=0
for y in range(255):
    print(R[y],"\n")          

cap.release()
