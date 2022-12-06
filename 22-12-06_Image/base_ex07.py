import cv2
import numpy as np
from utils import image_show_compare

img_path = 'car.png'
img = cv2.imread(img_path)

# 엠보싱 효과
filter1 = np.array([[0,1,0], [0,0,0], [0,-1,0]])
filter2 = np.array([[-1,-1,0], [-1,0,1], [0,1,1]])

emboss_img1 = cv2.filter2D(img, -1, filter1)
emboss_img2 = cv2.filter2D(img, -1, filter2)
# emboss_img1 = emboss_img1 + 128
# emboss_img2 = emboss_img2 + 128

image_show_compare(emboss_img1, emboss_img2)