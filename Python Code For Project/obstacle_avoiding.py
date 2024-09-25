import numpy as np
import math

difference = 0
def turn(theta):
    pass                                                                                                                                                                          
def go_to(x_coordinate, y_coordinate, x_to, y_to, speed):
    distance = math.sqrt((x_coordinate - x_to) ** 2 + (y_coordinate - y_to) ** 2)
    theta = np.arcsin(x_to, distance)
    turn(theta)

    

def manage_obstacle(distance, theta, difference):
    x_coordinate = distance * np.sin(theta)
    y_coordinate = distance * np.cos(theta)

    point_to_go = (x_coordinate, y_coordinate - difference)
