import cv2
import numpy as np


# Callback function for the trackbars, it does nothing but is required by the createTrackbar function
def nothing(x):
    pass


# Load the image or use the webcam
# For image:
# img = cv2.imread('path_to_image.jpg')

# For webcam:
cap = cv2.VideoCapture(0)

# Create a window named 'Trackbars'
cv2.namedWindow('Trackbars')

# Create trackbars for the lower and upper HSV limits
cv2.createTrackbar("LH", "Trackbars", 0, 179, nothing)  # Lower Hue
cv2.createTrackbar("LS", "Trackbars", 0, 255, nothing)  # Lower Saturation
cv2.createTrackbar("LV", "Trackbars", 0, 255, nothing)  # Lower Value
cv2.createTrackbar("UH", "Trackbars", 179, 179, nothing)  # Upper Hue
cv2.createTrackbar("US", "Trackbars", 255, 255, nothing)  # Upper Saturation
cv2.createTrackbar("UV", "Trackbars", 255, 255, nothing)  # Upper Value

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get current positions of trackbars
    lh = cv2.getTrackbarPos("LH", "Trackbars")
    ls = cv2.getTrackbarPos("LS", "Trackbars")
    lv = cv2.getTrackbarPos("LV", "Trackbars")
    uh = cv2.getTrackbarPos("UH", "Trackbars")
    us = cv2.getTrackbarPos("US", "Trackbars")
    uv = cv2.getTrackbarPos("UV", "Trackbars")

    # Define the lower and upper HSV limits
    lower_limit = np.array([lh, ls, lv])
    upper_limit = np.array([uh, us, uv])

    # Create a mask based on the defined limits
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, the mask, and the result
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
