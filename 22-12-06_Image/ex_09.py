import cv2
from utils import image_show

image_path = 'kuromi.jpg'
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 리사이즈
image_10x10 = cv2.resize(image_gray, (10,10))

# 이미지 데이터를 1차원 벡터로 변환
image_10x10.flatten()
image_show(image_10x10)
