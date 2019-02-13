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
frameR=cv2.resize(frame2, (400,400))
frameG=cv2.resize(frame2, (400,400))
frameB=cv2.resize(frame2, (400,400))
   
   
x=0
y=0
R=[] 
G=[]
B=[] 
for n in range(0,255):
    lower_rangeR = np.array([n, 0, 0])
    upper_rangeR = np.array([n+1, 255, 255])
    maskR = cv2.inRange(frameR, lower_rangeR, upper_rangeR)
    contourR = cv2.findContours(maskR,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    resG=cv2.bitwise_and(frameR,frameR,mask=maskR)
    #for pR in contourR:
    #cv2.drawContours(frameR, [pR], -1, (0,255,0), 3) 
    for cR in contourR:
       x+=cv2.contourArea(cR)
    R.append(x)
    x=0
n=0
x=0
for n in range(0,255):
    lower_rangeG = np.array([0, n, 0])
    upper_rangeG = np.array([255, n+1, 255])
    maskG = cv2.inRange(frameG, lower_rangeG, upper_rangeG)
    contourG = cv2.findContours(maskG,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    resG=cv2.bitwise_and(frameG,frameG,mask=maskG)
    #for pG in contourG:
    #cv2.drawContours(frameG, [pG], -1, (0,255,0), 3) 
    for cG in contourG:
       x+=cv2.contourArea(cG)
    G.append(x)
    x=0
n=0
x=0
for n in range(0,255):
    lower_rangeB = np.array([0, 0, n])
    upper_rangeB = np.array([255, 255, n+1])
    maskB = cv2.inRange(frameB, lower_rangeB, upper_rangeB)
    contourB = cv2.findContours(maskB,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    resB=cv2.bitwise_and(frameB,frameB,mask=maskB)
    #for pB in contourB:
    #cv2.drawContours(frameB, [pB], -1, (0,255,0), 3) 
    for cB in contourB:
       x+=cv2.contourArea(cB)
    B.append(x)
    x=0
for y in range(255):
    print(R[y]," ",G[y]," ",B[y],"\n")            

cap.release()
