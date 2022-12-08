# 같은 크기의 이미지 블렌딩 실험
import cv2
import matplotlib.pyplot as plt
import numpy as np

large_img = cv2.imread('ex_image.png')
wartermark = cv2.imread('ex_image_logo.png')

print(large_img.shape)
print(wartermark.shape)

img1 = cv2.resize(large_img, (800,600))
img2 = cv2.resize(wartermark, (800,600))

print('img1 resize >> ', img1.shape)
print('img2 resize >> ', img2.shape)

### 혼합 진행

# 베이스 5:5
blended = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow('image show', blended)
cv2.waitKey(0)

# # 베이스 9:1
# blended = cv2.addWeighted(img1, 0.9, img2, 0.1, 0)
# cv2.imshow('image show', blended)
# cv2.waitKey(0)

# # 베이스 1:1
# blended = cv2.addWeighted(img1, 1, img2, 1, 0)
# cv2.imshow('image show', blended)
# cv2.waitKey(0)