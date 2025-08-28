import cv2
import time
import numpy as np

# Load the car cascade classifier
car_classifier_path = r"D:\Samson - All Data\Open cv\haarcascade_car.xml"
car_classifier = cv2.CascadeClassifier(car_classifier_path)

# Video path
video_path = r"D:\Samson - All Data\Open cv\Moving car.avi"

# Load the video
cap = cv2.VideoCapture(video_path)

# Loop once video is successfully loaded
while cap.isOpened():
    time.sleep(0.05)  # control frame speed
    
    # Read frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    # Detect cars
    cars = car_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    
    # Draw bounding boxes for cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    
    # Display the frame with detected cars
    cv2.imshow("Cars Dection", frame)

    # Exit the loop when the Enter key is pressed
    if cv2.waitKey(1) ==13: # 13 is the Enter key
        print("Exiting...")
        break
    
# Optional: Add a small delay between frames (to make the processing smoother)
time.sleep(0.05)

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
