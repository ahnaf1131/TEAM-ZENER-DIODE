import cv2
import numpy as np

# Define HSV limits for yellow
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# Define HSV limits for red (two ranges, as red spans the HSV spectrum)
lower_red_1 = np.array([0, 100, 100])
upper_red_1 = np.array([10, 255, 255])
lower_red_2 = np.array([170, 100, 100])
upper_red_2 = np.array([180, 255, 255])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask for yellow
    mask_yellow = cv2.inRange(hsvImage, lower_yellow, upper_yellow)

    # Create masks for red (two ranges)
    mask_red_1 = cv2.inRange(hsvImage, lower_red_1, upper_red_1)
    mask_red_2 = cv2.inRange(hsvImage, lower_red_2, upper_red_2)

    # Combine the two red masks
    mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)

    # Find contours for yellow objects
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw bounding boxes for yellow objects
    for contour in contours_yellow:
        if cv2.contourArea(contour) > 500:  # Filter out small objects based on area
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Yellow color box

    # Find contours for red objects
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw bounding boxes for red objects
    for contour in contours_red:
        if cv2.contourArea(contour) > 500:  # Filter out small objects based on area
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red color box

    # Display the frame with the bounding boxes
    cv2.imshow('frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
