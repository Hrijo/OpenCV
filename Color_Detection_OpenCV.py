from cv2 import waitKey
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # lower_blue = np.array([50,50,50])  # Trial lower limit 1
    # upper_blue = np.array([130,255,255]) # Trail upper limit 1

    # lower_blue = np.array([0,0,0]) # Trail lower limit 2
    # upper_blue = np.array([243,0,20]) # Trial upper limit 2
    
    lower_blue = np.array([90,50,50]) # Trial lower limit Final
    upper_blue = np.array([130,255,255]) # Trial upper limit Final

    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    cv2.imshow('raw',frame)
    if waitKey(1) == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()