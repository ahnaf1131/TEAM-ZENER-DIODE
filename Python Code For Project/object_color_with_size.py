# import cv2
# import numpy as np


# # Define HSV limits for yellow
# lower_green = np.array([30, 50, 50]) 
# upper_green = np.array([90, 255, 255]) 






# # Define HSV limits for red (two ranges, as red spans the HSV spectrum)
# lower_red_1 = np.array([0, 100, 100])
# upper_red_1 = np.array([10, 255, 255])
# lower_red_2 = np.array([170, 100, 100])
# upper_red_2 = np.array([180, 255, 255])

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert the frame to HSV color space
#     hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # Create mask for yellow
#     mask_yellow = cv2.inRange(hsvImage, lower_green, upper_green)

#     # Create masks for red (two ranges)
#     mask_red_1 = cv2.inRange(hsvImage, lower_red_1, upper_red_1)
#     mask_red_2 = cv2.inRange(hsvImage, lower_red_2, upper_red_2)

#     # Combine the two red masks
#     mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)


#     # Function to draw bounding box and estimate size
#     def draw_and_estimate_size(mask, frame, color_name, box_color):
#         contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         for contour in contours:
#             if cv2.contourArea(contour) > 500:  # Filter out small objects based on area
#                 x, y, w, h = cv2.boundingRect(contour)
#                 # Draw bounding box
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, 2)

#                 # Estimate size (area of the bounding box)
#                 size = w * h
#                 size_text = f"{color_name} size: {size} px"

#                 # Display the estimated size on the frame
#                 cv2.putText(frame, size_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)


#     # Draw and estimate size for yellow objects
#     draw_and_estimate_size(mask_yellow, frame, "Green", (0, 255, 0))  # Green bounding box

#     # Draw and estimate size for red objects
#     draw_and_estimate_size(mask_red, frame, "Red", (0, 0, 255))  # Red bounding box

#     # Display the frame with bounding boxes and size estimations
#     cv2.imshow('frame', frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np
import math

# Known object dimensions in meters
REAL_HEIGHT = 0.1  # 100 mm
REAL_WIDTH = 0.05  # 50 mm

# Lenovo IdeaPad 1 camera specifications (these may need calibration)
FOCAL_LENGTH_MM = 3.7  # Focal length in mm
SENSOR_WIDTH_MM = 4.54  # Sensor width in mm
SENSOR_HEIGHT_MM = 3.42  # Sensor height in mm

# Convert focal length from mm to pixels
FOCAL_LENGTH_PIXELS = (FOCAL_LENGTH_MM / SENSOR_WIDTH_MM) * 800  # Example scaling factor for 800px width

# Define HSV limits for green
lower_green = np.array([25, 40, 40]) 
upper_green = np.array([100, 255, 255]) 

# Define HSV limits for red (two ranges, as red spans the HSV spectrum)
lower_red_1 = np.array([150, 30, 30])
upper_red_1 = np.array([190, 255, 255])
lower_red_2 = np.array([150, 30, 30])
upper_red_2 = np.array([190, 255, 255])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Get frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Calculate the center of the frame
    center_x = frame_width // 2
    center_y = frame_height // 2

    # Convert the frame to HSV color space
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask for green
    mask_green = cv2.inRange(hsvImage, lower_green, upper_green)

    # Create masks for red (two ranges)
    mask_red_1 = cv2.inRange(hsvImage, lower_red_1, upper_red_1)
    mask_red_2 = cv2.inRange(hsvImage, lower_red_2, upper_red_2)
    
    # Combine the two red masks
    mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)

    # Function to draw bounding box, detect center point, calculate distance, and angle
    def draw_detect_center_distance_and_angle(mask, frame, color_name, box_color):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filter out small objects based on area
                x, y, w, h = cv2.boundingRect(contour)

                # Check if the object has fallen (height < width)
                if h < w:
                    h, w = w, h  # Flip height and width

                # Calculate the center of the object
                cx = x + w // 2
                cy = y + h // 2

                # Calculate the center point relative to the vertical center of the screen
                cx_relative = cx - center_x

                # Calculate distance using the pinhole camera model
                if h > 0:  # Avoid division by zero
                    distance = (FOCAL_LENGTH_PIXELS * REAL_HEIGHT) / h
                else:
                    distance = 0

                # Calculate the angle between the object's center and the vertical center line
                angle_horizontal = math.degrees(math.atan2(cx_relative, FOCAL_LENGTH_PIXELS))

                # **Remove normalization**; the angle will now exceed 180 and -180 if necessary.

                # Draw bounding box
                cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, 2)

                # Draw center point
                cv2.circle(frame, (cx, cy), 5, box_color, -1)

                # Display the relative center coordinates and horizontal angle
                angle_text = f"{color_name} Angle: {angle_horizontal:.2f}°"
                cv2.putText(frame, angle_text, (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)

                # Display the estimated distance of the object
                distance_text = f"Distance: {distance:.2f} meters"
                cv2.putText(frame, distance_text, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)

    # Draw, detect center, and estimate distance and angle for green objects
    draw_detect_center_distance_and_angle(mask_green, frame, "Green", (0, 255, 0))  # Green bounding box

    # Draw, detect center, and estimate distance and angle for red objects
    draw_detect_center_distance_and_angle(mask_red, frame, "Red", (0, 0, 255))  # Red bounding box

    # Display the frame with bounding boxes, center points, distances, and angles
    cv2.imshow('frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
