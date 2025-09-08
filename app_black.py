import cv2
import numpy as np
import streamlit as st

st.title("🎨 Real-time Color Detection with OpenCV + Streamlit")

# Start webcam
cap = cv2.VideoCapture(0)

# Streamlit placeholder for video frames
frame_window = st.empty()
red_window = st.empty()
blue_window = st.empty()
green_window = st.empty()
result_window = st.empty()

# Button to stop
stop_button = st.button("Stop Camera")

while cap.isOpened() and not stop_button:
    ret, frame = cap.read()
    if not ret:
        st.write("Failed to grab frame")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red mask
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Blue mask
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Green mask
    low_green = np.array([40, 100, 100])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Convert BGR (OpenCV) → RGB (Streamlit)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    red_rgb = cv2.cvtColor(red, cv2.COLOR_BGR2RGB)
    blue_rgb = cv2.cvtColor(blue, cv2.COLOR_BGR2RGB)
    green_rgb = cv2.cvtColor(green, cv2.COLOR_BGR2RGB)
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    # Show in Streamlit
    frame_window.image(frame_rgb, caption="Original Frame")
    red_window.image(red_rgb, caption="Red Detection")
    blue_window.image(blue_rgb, caption="Blue Detection")
    green_window.image(green_rgb, caption="Green Detection")
    result_window.image(result_rgb, caption="Other Colors")

cap.release()
