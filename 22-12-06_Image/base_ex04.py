import cv2
import numpy as np
from utils import image_show

image = cv2.imread('car.png')

# creating maxican hat filter for
# 5x5
filter = np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]])
mexican_hat_image1 = cv2.filter2D(image, -1, filter)

# 3x3
filter = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
mexican_hat_image2 = cv2.filter2D(image, -1, filter)

cv2.imwrite('mexican_hat_5x5.png', mexican_hat_image1)
cv2.imwrite('mexican_hat_3x3.png', mexican_hat_image2)

cv2.imshow('mexican_hat_5x5', mexican_hat_image1)
cv2.imshow('mexican_hat_3x3', mexican_hat_image2)
cv2.waitKey(0)

