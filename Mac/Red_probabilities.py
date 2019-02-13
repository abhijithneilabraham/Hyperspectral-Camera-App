
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
        frame1R=cv2.resize(frame2,(720,1080))
        frame1G=cv2.resize(frame2,(720,1080))
        frame1B=cv2.resize(frame2,(720,1080))
        cv2.imshow("frame1",frame1R)
           
           
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
        xR=0
        xB=0
        xG=0
        yR=0
        yG=0
        yB=0
        
        area=[]
        R=[]#arrays for red,blue and green areas
        G=[]
        B=[] 
        for n in range(0,255):
            #hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
            lower_rangeR = np.array([n, 0, 0])
            upper_rangeR = np.array([n+1, 255, 255])
            #lower_range1 = cv2.cvtColor(lower_range, cv2.COLOR_HSV2BGR)
            #upper_range1 = cv2.cvtColor(upper_range, cv2.COLOR_HSV2BGR)
            maskR = cv2.inRange(frame1R, lower_rangeR, upper_rangeR)
            contourR = cv2.findContours(maskR,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
            #resR=cv2.bitwise_and(frame1,frame1,mask=mask)
            #for pR in contourR:
                #cv2.drawContours(frame1R, [pR], -1, (0,255,0), 3)
            cv2.imshow("mask",maskR)
            #cv2.imshow("res",res)  
            for cR in contourR:
               xR+=cv2.contourArea(cR)
            R.append(xR)
            xR=0
    
        for n in range(0,255):
            #hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
            lower_rangeG = np.array([0, n, 0])
            upper_rangeG = np.array([255, n+1, 255])
            #lower_range1 = cv2.cvtColor(lower_range, cv2.COLOR_HSV2BGR)
            #upper_range1 = cv2.cvtColor(upper_range, cv2.COLOR_HSV2BGR)
            maskG = cv2.inRange(frame1G, lower_rangeG, upper_rangeG)
            contourG = cv2.findContours(maskG,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
            #res=cv2.bitwise_and(frame1,frame1,mask=mask)
            #for pG in contourG:
                #cv2.drawContours(frame1G, [pG], -1, (0,255,0), 3)
            cv2.imshow("mask",maskG)
            #cv2.imshow("res",res)  
            for cG in contourG:
               xG+=cv2.contourArea(cG)
            B.append(xG)
            x=0
        
        for n in range(0,255):
            #hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
            lower_rangeB = np.array([0, 0, n])
            upper_rangeB= np.array([255, 255, n+1])
            #lower_range1 = cv2.cvtColor(lower_range, cv2.COLOR_HSV2BGR)
            #upper_range1 = cv2.cvtColor(upper_range, cv2.COLOR_HSV2BGR)
            maskB = cv2.inRange(frame1B, lower_rangeB, upper_rangeB)
            contourB = cv2.findContours(maskB,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
            #res=cv2.bitwise_and(frame1,frame1,mask=mask)
            #for pB in contourB:
                #cv2.drawContours(frame1B, [pB], -1, (0,255,0), 3)
            cv2.imshow("mask",maskB)
            #cv2.imshow("res",res)  
            for cB in contourB:
               xB+=cv2.contourArea(cB)
            G.append(xB)
            xB=0
        for y in range(255):
           
            #area=cv2.contourArea(contourR)
               
            print(R[y]," , ",G[y]," , ",B[y],"  \n")     
    counter=counter-1
                       
    


# When everything done, release the capture
cap.release()


cv2.destroyAllWindows()
