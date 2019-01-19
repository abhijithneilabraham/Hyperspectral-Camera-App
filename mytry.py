#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 02:12:50 2019

@author: abhijithneilabraham
"""


import cv2
cap = cv2.VideoCapture(0)
r=0
b=0
g=0
while(True):
  # Capture frame-by-frame
   ret, frame = cap.read()
   '''
   # Our operations on the frame come here
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   blur = cv2.GaussianBlur(gray,(5,5),5)
   ret, thresh_img = cv2.threshold(blur,91,255,cv2.THRESH_BINARY)
   contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
   
   for c in contours:
      
        cv2.drawContours(frame, [c], -1, (0,255,0), 3)
       
       a,b=cv2.split(c)
       print(a[0],b[0])
   '''   

     # Display the resulting frame
   frame = cv2.rectangle(frame,(450,180),(800,540),(0,255,0),1)
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
      break
   
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
   print(hsv)                  



# When everything done, release the capture
cap.release()


cv2.destroyAllWindows()



