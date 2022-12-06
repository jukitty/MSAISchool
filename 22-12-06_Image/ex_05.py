import cv2
from utils import image_show

# 이미지 경로
image_path = 'cat.jpg'

# 이미지 이진화
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) # RGB -> Gray
max_output_value = 255 # color : 0~255
neighborhood_size = 99
subtract_from_mean = 10

image_binary = cv2.adaptiveThreshold(image_gray,
                                     max_output_value,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY,
                                     neighborhood_size,
                                     subtract_from_mean
                                     ) # 이진화할때 가장 많이 사용하는 함수
image_show(image_binary)