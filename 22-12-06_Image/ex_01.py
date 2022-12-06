# 이미지 blur 처리
# filter 2d() 메소드 사용
import cv2
import numpy as np

from utils import image_show

# 이미지 경로
image_path = 'cat.jpg'

# 이미지 읽어오기
image = cv2.imread(image_path)

# 커널 생성 처리
kernel = np.ones((10, 10)) / 25.0  # 1로 전부 채우기. 모두 더하면 1이 되도록 정규화
image_kernel = cv2.filter2D(image, -1, kernel) # 이미지, depth, 커널

image_show(image_kernel)