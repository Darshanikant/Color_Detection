import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    low_red_1 = np.array([161, 155, 84])
    high_red_1 = np.array([179, 255, 255])

    #red color upper
    low_red = np.array([160, 150, 80])
    high_red = np.array([180, 255, 255])
    
    red_mask=cv2.inRange(hsv_frame, low_red, high_red)
    
    red=cv2.bitwise_and(frame, frame, mask=red_mask)
    
    cv2.imshow("frame", frame)
    
    cv2.imshow('red mask', red)
    
    key =cv2.waitKey(1)
    if key==27:
        break
    