import numpy as np
import cv2

# Load the face and eye Haar cascade classifiers
face_classifier = cv2.CascadeClassifier(r"D:\Samson - All Data\Open cv\haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier(r"D:\Samson - All Data\Open cv\haarcascade_eye.xml")

# Load the image
img = cv2.imread(r"D:\Samson - All Data\Samson resume\Samson image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# Draw rectangle around detected faces and detect eyes within each face
for (x, y, w, h) in faces:
    # Draw rectangle around the face
    cv2.rectangle(img, (x, y), (x + w, y + h), (127, 0, 255), 2)
    
    # Region of interest (ROI) for face
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    
    # Detect eyes within the face region
    eyes = eye_classifier.detectMultiScale(roi_gray)
    
    for (ex, ey, ew, eh) in eyes:
        # Draw rectangle around the eyes
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
        
# Display the output image with rectangles around faces and eyes
cv2.imshow('img', img)

# Wait for a key press before closing the window
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()