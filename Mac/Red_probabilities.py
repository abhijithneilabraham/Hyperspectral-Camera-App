

import cv2
import numpy as np
from time import sleep
cap = cv2.VideoCapture(0)

 # Capture frame-by-frame
'''
 going to simply add a program to find the different screen resolutions that might arise in different systems
 this might help in drawing the roi
'''
ret, frame = cap.read()

print(len(frame),len(frame[0]))#to get the screen resolution of the device we are using.

r=0
b=0
g=0
counter=2


while(counter>0):
    
    
    
    
  # Capture frame-by-frame
    cap.grab()
    retval, fr = cap.retrieve(0)
    if counter<2: #this is done for mac ,the first frame is fully black.
         
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
              
        
        # Display the resulting frame
        '''
        
        cv2.imshow("frame",fr)
        frame2 = fr[450:800,180:540]
        cv2.imshow("frame2",frame2)
        frame1=cv2.resize(frame2,(720,1080))
        cv2.imshow("frame1",frame1)
           
           
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
        x=0
        y=0
        area=[]
        R=[]
        G=[]
        B=[] 
        for n in range(0,255):
            #hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
            lower_range = np.array([n, 0, 0])
            upper_range = np.array([n+1, 255, 255])
            #lower_range1 = cv2.cvtColor(lower_range, cv2.COLOR_HSV2BGR)
            #upper_range1 = cv2.cvtColor(upper_range, cv2.COLOR_HSV2BGR)
            mask = cv2.inRange(frame1, lower_range, upper_range)
            contour = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
            res=cv2.bitwise_and(frame1,frame1,mask=mask)
            for p in contour:
                cv2.drawContours(frame1, [p], -1, (0,255,0), 3)
            cv2.imshow("mask",mask)
            cv2.imshow("res",res)  
            for c in contour:
               x+=cv2.contourArea(c)
            area.append(x)
            x=0
        for y in range(255):
           print(area[y],"\n")          
            #area=cv2.contourArea(contourR)
               
        #print(R," , ",G," , ",B,"  \n",n)     
    counter=counter-1
                       
    


# When everything done, release the capture
cap.release()


cv2.destroyAllWindows()
