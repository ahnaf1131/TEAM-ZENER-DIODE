import cv2
import numpy as np


def color_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    # loLim = hsvC[0][0][0] - 44, 100, 100
    # uLim = hsvC[0][0][0] + 64, 255, 255

    loLim_yellow = np.array([20, 100, 109])
    uLim_yellow = np.array([35, 221, 255])

    loLim_red = np.array([143, 127, 122])
    uLim_red = np.array([179, 255, 255])

    return loLim_yellow,uLim_yellow,loLim_red,uLim_red



