import cv2
import numpy as np
from utils import image_show

image = cv2.imread('car.png')

filter = np.array([[-3,-1,-7], [-1,8,-1], [1,-1,5]])
custom_image_filter = cv2.filter2D(image, -1, filter)

image_show(custom_image_filter)