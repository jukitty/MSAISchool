import cv2
from utils import image_show
import numpy as np

image_path = 'kuromi.jpg'
image = cv2.imread(image_path)

# image 20x20픽셀 크기로 변환
image_color_20x20 = cv2.resize(image, (20,20))

# flatten
image_color_20x20.flatten()
#image_show(image_color_20x20)

# image 255x255 픽셀 크기로 변환
image_color_225x255 = cv2.resize(image, (225,255))
image_color_225x255.flatten()
image_show(image_color_225x255)

# # 2차원 배열을 1차원으로
# x = np.array([[51,40], [34,35], [2,94]])
# x = x.flatten()
# print(x)