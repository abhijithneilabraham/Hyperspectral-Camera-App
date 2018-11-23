import numpy as np
import cv2


cap = cv2.VideoCapture(0)
r=0
b=0
g=0
while(True):
  # Capture frame-by-frame
   ret, frame = cap.read()

   # Our operations on the frame come here
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   blur = cv2.GaussianBlur(gray,(5,5),0)
   ret, thresh_img = cv2.threshold(blur,91,255,cv2.THRESH_BINARY)
   contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
   for c in contours:
        cv2.drawContours(frame, [c], -1, (0,255,0), 3)

     # Display the resulting frame
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
      break
   for i in range(0,479):
       for j in range(0,479):
           color = frame[i,j]
           r=r+color[0]
           g=g+color[1]
           b=b+color[2]
   print("r=",r/230400)
   print("g=",g/230400)
   print("b=",b/230400)
   r=0
   b=0
   g=0


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
