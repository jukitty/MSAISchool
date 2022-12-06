# 배경 제거
import cv2
import numpy as np
import matplotlib.pyplot as plt

from utils import image_show

image_path = 'kuromi.jpg'
image = cv2.imread(image_path)
# print(image.shape) = (512, 512, 3)

# 사각형 크기 좌표, 사각형의 시작점 : x, y ,넓이, 높이
rectangle = (0, 0, 500, 500)
mask = np.zeros(image.shape[:2], np.uint8)

# grabCut에 사용할 임시 배열 생성
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# grabCut 실행
# image -> 원본이미지, bgdModel -> 배경을 위한 임시배열, fgdModel -> 전경 배경, 5회 반복, 사각형 초기화
cv2.grabCut(image, mask, rectangle, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# 배경인 곳 : 0, 그 외 : 1 로 설정한 마스크
mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

# 이미지에 새로운 마스크를 곱해서 배경 제외하기
image_rgb_nobg = image * mask_2[:, :, np.newaxis]
# image_show(image_rgb_nobg)

cv2.imshow('Original Image', image)
cv2.imshow('No background Image', image_rgb_nobg)
cv2.waitKey(0)