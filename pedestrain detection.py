import cv2
import numpy as np
import os

# Set the path for the body classifier (Haar Cascade XML)
body_classifier_path = r"D:\Samson - All Data\Open cv\haarcascade_fullbody.xml"

# Create the body classifier using the provided path
body_classifier = cv2.CascadeClassifier(body_classifier_path)

# Set the path for the video file
video_path = r"D:\Samson - All Data\Open cv\moving.avi"

# Open the video file
cap = cv2.VideoCapture(video_path)

# Read a frame from the video
ret, frame = cap.read()

# Convert the frame to grayscale for better detection performance
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect bodies in the grayscale image
bodies = body_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# Draw bounding boxes around detected bodies
for (x, y, w, h) in bodies:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    
# Display the result with detected bodies
cv2.imshow("Pedestrians", frame)

# Press Enter (13) to exit
if cv2.waitKey(0) == 13:  # 13 corresponds to the Enter key
    print("Exiting...")

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

