# 모서리 감지
import numpy as np
import cv2
from utils import image_show

image_path = 'test1.png'

image_read = cv2.imread(image_path)

# 이미지 읽기
image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
image_gray = np.float32(image_gray)

# 모서리 찾기
block_size = 2 # 모서리 감지 매개변수 설정
aperture = 29
free_parameter = 0.04

detector_response = cv2.cornerHarris(image_gray, block_size, aperture, free_parameter)

print(detector_response)

threshold = 0.02
image_read[detector_response > threshold * detector_response.max()] = [255, 255, 255]
image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
image_show(image_gray)