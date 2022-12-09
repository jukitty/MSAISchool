import numpy as np
import cv2

# 이미지 경로
x = cv2.imread('cat.jpg',0) # 0:흑백
y = cv2.imread('cat.jpg',1) # 1:color

## 리사이즈 (원본 비율 지켜지지x)
# img = cv2.resize(x, (200,200))
# cv2.imshow('Cat image show gray', img)

## 윈도우 창
# cv2.imshow('Cat image show gray', x)
# cv2.imshow('Cat image show color', y)
# cv2.waitKey(0)

# 여러개 파일 save .npz
np.savez('./image.npz', array1=x, array2=y)

# 압축 방법
np.savez_compressed('./image_compressed.npz', array1=x, array2=y)

# .npz 데이터 로드
data = np.load('image_compressed.npz')

result1 = data['array1']
result2 = data['array2']

cv2.imshow('result1', result1)
cv2.waitKey(0) # 이미지:0 , 동영상:1 (프레임이기 때문에)
