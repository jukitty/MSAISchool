import cv2
import numpy as np
from utils import image_show

# 이미지 읽기
image = cv2.imread('kuromi.jpg')

# 경계선 찾기
# canny() -> 무조건 gray scale로
image_gray = cv2.imread('kuromi.jpg', cv2.IMREAD_GRAYSCALE)

# 픽셀 강도의 중간값 찾기
median_intensity = np.median(image_gray)

# 중간 픽셀 강도에서 위 아래 1 표준편차 떨어진 값을 임계값으로 설정
lower_threshold = int(max(0, (1.0 - 0.45) * median_intensity))
upper_threshold = int(max(225, (1.0 + 0.45) * median_intensity))

# Canny edge Detection 적용
image_canny = cv2.Canny(image_gray, lower_threshold, upper_threshold)
image_show(image_canny)