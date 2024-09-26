import cv2
import numpy as np

# Define HSV ranges for blue and yellow
blue_lower = np.array([104, 119, 110])
blue_upper = np.array([113, 255, 183])

yellow_lower = np.array([11, 141, 208])
yellow_upper = np.array([17, 242, 254])


def detect_first_color(image_path):
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    # Convert to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Get the dimensions of the image
    height, width, _ = hsv_image.shape

    # Scan each row to detect the first appearance of blue or yellow
    for y in range(height):
        for x in range(width):
            pixel_hsv = hsv_image[y, x]

            # Check if the pixel is blue
            if blue_lower[0] <= pixel_hsv[0] <= blue_upper[0] and \
                    blue_lower[1] <= pixel_hsv[1] <= blue_upper[1] and \
                    blue_lower[2] <= pixel_hsv[2] <= blue_upper[2]:
                print("Rule: r (Blue first)")
                return 'r'

            # Check if the pixel is yellow
            if yellow_lower[0] <= pixel_hsv[0] <= yellow_upper[0] and \
                    yellow_lower[1] <= pixel_hsv[1] <= yellow_upper[1] and \
                    yellow_lower[2] <= pixel_hsv[2] <= yellow_upper[2]:
                print("Rule: l (Yellow first)")
                return 'l'

    # If no color was detected, return None
    print("No blue or yellow detected.")
    return None


# Example usage
image_path = '1.jpg'  # Path to the image
detect_first_color(image_path)
