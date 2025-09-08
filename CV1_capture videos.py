import cv2 # package of AI
import numpy as np

#Lets capture the camera. 0 for webcam. if you want other webcam then we can change to ind
cap = cv2.VideoCapture(0)

#Lets load the frame
while True:
    _, frame = cap.read()
    
    # we convert this format to hav , bgr library this is color format red, green, blue, we
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
# Lets frame on the windows
    cv2.imshow("Frame", frame)
    
# weight key event which is 1 and which is 27 then break the loop that means we are going
    key = cv2.waitKey(1)
    if key == 27:
        break
    
# Lets run this one and we will see the camera, camera is on

# Now lets deeper understanding how to detect color now

''' HSV --> HUE - we can see the color red,green,blue,yellow and also we can see the gradio
         SATURATION - How much quantity of the color we want to have
         (0- nothing, completely white, opencv - maximum pixel 0-255)
         VALUE - Brightness of the color (0- completely black)'''