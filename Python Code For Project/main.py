import coordination as cd

direction = 'left'

def detect_object_positions():
    return x_obj, y_obj


def detect_object_color():
    return color


def get_magnetometer_values():
    magneto_x, magneto_y = 0, 0
    return magneto_x, magneto_y
def detect_own_position():
    x_value, y_value = 0, 0
    return x_value, y_value

def get_direction(color_of_line):
    direction = 'left'
    return direction
def start_turning(x_obstacle, y_obstacle):
    pass
section_count = 0

while section_count <= 11:
    magneto_x, magneto_y = get_magnetometer_values()
    init_theta = cd.calculate_initial_theta(magneto_x, magneto_y)
    theta = 0
    while theta < 90:
        magneto_x, magneto_y = get_magnetometer_values()
        theta = cd.calculate_theta_difference(init_theta, magneto_x, magneto_y)
        x_value, y_value = cd.calculate_theta_XY(direction, theta)
        x_obj, y_obj = detect_object_positions()
        color = detect_object_color()
        start_turning()
