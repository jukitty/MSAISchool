'''
Gradient : detect edge (dilation - erosion)  엣지 강조해서 연산하는 방법
Tophat : original - opening  밝기애서 밝은 부분 차이 강조
Blockhot : closing - original  어두운 부분 차이 강조
opening : dilation @ erosion  노이즈 제거
closing : erosion @ dilation  객체 바운더리 생성
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Billiards.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

op_idx = {
    'gradient': cv2.MORPH_GRADIENT,
    'tophat': cv2.MORPH_TOPHAT,
    'blackhat': cv2.MORPH_BLACKHAT
}

def onChange(k, op_name):
    if k == 0:
        cv2.imshow(op_name, mask)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
    dst = cv2.morphologyEx(mask, op_idx[op_name], kernel)
    cv2.imshow(op_name, dst)

cv2.imshow('Origin', img)
cv2.imshow('gradient', mask)    # 엣지 강조해서 연산하는 방법
cv2.imshow('tophat', mask)      # 밝기애서 밝은 부분 차이 강조
cv2.imshow('blackhat', mask)    # 어두운 부분 차이 강조


cv2.createTrackbar('k', 'gradient', 0, 300,lambda x:onChange(k=x, op_name='gradient'))
cv2.createTrackbar('k', 'tophat', 0, 300,lambda x:onChange(k=x, op_name='tophat'))
cv2.createTrackbar('k', 'blackhat', 0, 300,lambda x:onChange(k=x, op_name='blackhat'))

cv2.waitKey(0)
cv2.destroyAllWindows()