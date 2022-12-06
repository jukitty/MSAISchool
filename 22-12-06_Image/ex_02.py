# 가우시안 블러
import cv2
from utils import image_show

#이미지 경로
image_path = 'cat.jpg'

# 이미지 읽기
image = cv2.imread(image_path)

image_g_blury = cv2.GaussianBlur(image, (10,10), 0)
image_show(image_g_blury)