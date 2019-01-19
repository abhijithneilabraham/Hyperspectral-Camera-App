import cv2
import numpy as np

cap = cv2.VideoCapture(0)#video

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    '''
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    '''
    # define range of blue color in HSV(hue saturation value)
    lower_blue = np.array([0,0,0])
    upper_blue = np.array([255,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(frame, lower_blue, upper_blue)
    

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    print(res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()