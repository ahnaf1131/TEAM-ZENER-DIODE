import math

# take input from lidar or ultrasonic sensors
frontDistance = 0
leftDistance = 0
rightDistance = 0
backDistance = 0

# take input from magnetic  senser for direcion
thetaX = 0
thetaY = 0
thetaZ = 0
thetaDifferenceInDegree = 0

# All distance sensors
distance_sensors_right = ['lider', 'left_sonar', 'back_sonar', 'right_sonar']
x_sensor_right = distance_sensors_right[1]
y_sensor_right = distance_sensors_right[0]


# import math
#
#
# def calculate_heading(x, y, initial_heading=0):
#     # Calculate angle in radians
#     heading_rad = math.atan2(y, x)
#
#     # Convert to degrees
#     heading_deg = math.degrees(heading_rad)
#
#     # Normalize to 0-360 degrees
#     heading_deg = (heading_deg + 360) % 360
#
#     # Adjust by initial heading
#     heading_deg = (heading_deg - initial_heading + 360) % 360
#
#     return heading_deg
#
#
# # Example usage
# x = 000  # Replace with actual X-axis value
# y = 0  # Replace with actual Y-axis value
# initial_heading = 100  # Set your initial heading here
# heading = calculate_heading(x, y, initial_heading)
# print(f"Heading: {heading:.2f} degrees")


def calculate_initial_theta(magnetometer_x, magnetometer_y):
    # Calculate angle in radians
    initial_rad = math.atan2(magnetometer_y, magnetometer_x)

    # Convert to degrees
    initial_deg = math.degrees(initial_rad)

    # Normalize to 0-360 degrees
    initial_deg = (initial_deg + 360) % 360

    return initial_deg


def calculate_theta_difference(initial_deg, magnetometer_x, magnetometer_y):
    # Calculate angle in radians
    new_rad = math.atan2(magnetometer_y, magnetometer_x)

    # Convert to degrees
    new_deg = math.degrees(new_rad)
    #
    # # Normalize to 0-360 degrees
    new_deg = (initial_deg + 360) % 360

    theta_difference_in_degree = new_deg - initial_deg
    return theta_difference_in_degree


def calculate_initial_XY(direction, front_distance, left_distance, right_distance):
    if direction == "left":
        return front_distance, right_distance
    else:
        return front_distance, left_distance


def calculate_theta_XY(direction, theta_difference_in_degree):
    theta_difference_in_degree = math.radians(theta_difference_in_degree)
    x_value = math.cos(theta_difference_in_degree) * frontDistance
    if direction == "left":
        y_value = math.cos(theta_difference_in_degree) * rightDistance
    else:
        y_value = math.cos(theta_difference_in_degree) * leftDistance

    return x_value, y_value


# def change_sensor(theta_difference_in_degree, x_sensor, y_sensor, distance_sensors):
#     if theta_difference_in_degree >= 90 and theta_difference_in_degree < 180:
#         new_x_sensor = distance_sensors[distance_sensors.index(x_sensor) + 1]
#         new_y_sensor = distance_sensors[distance_sensors.index(y_sensor) + 1]
#     elif theta_difference_in_degree >= 180:



# Example usage
x = 1  # Replace with actual X-axis value
y = 0.577  # Replace with actual Y-axis value
heading = calculate_initial_theta(x, y)
print(f"Heading: {heading:.2f} degrees")
