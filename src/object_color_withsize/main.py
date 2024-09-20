import cv2
import numpy as np


# Define HSV limits for yellow
lower_green = np.array([30, 50, 50]) 
upper_green = np.array([90, 255, 255]) 

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
    mask_yellow = cv2.inRange(hsvImage, lower_green, upper_green)

    # Create masks for red (two ranges)
    mask_red_1 = cv2.inRange(hsvImage, lower_red_1, upper_red_1)
    mask_red_2 = cv2.inRange(hsvImage, lower_red_2, upper_red_2)

    # Combine the two red masks
    mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)


    # Function to draw bounding box and estimate size
    def draw_and_estimate_size(mask, frame, color_name, box_color):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filter out small objects based on area
                x, y, w, h = cv2.boundingRect(contour)
                # Draw bounding box
                cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, 2)

                # Estimate size (area of the bounding box)
                size = w * h
                size_text = f"{color_name} size: {size} px"

                # Display the estimated size on the frame
                cv2.putText(frame, size_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)


    # Draw and estimate size for yellow objects
    draw_and_estimate_size(mask_yellow, frame, "Green", (0, 255, 0))  # Green bounding box

    # Draw and estimate size for red objects
    draw_and_estimate_size(mask_red, frame, "Red", (0, 0, 255))  # Red bounding box

    # Display the frame with bounding boxes and size estimations
    cv2.imshow('frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

             

