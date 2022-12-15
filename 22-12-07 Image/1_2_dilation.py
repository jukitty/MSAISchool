import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Billiards.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

# kernel shape
kernel = []
for i in [cv2.MORPH_RECT, cv2.MORPH_CROSS, cv2.MORPH_ELLIPSE]: # 사각형 모형
    kernel.append(cv2.getStructuringElement(i, (11, 11)))

# print(kernel[2]) # 타원형. 커널 값에 따라서 객체 모형이 바뀐다.

title = ['Rectangle', 'Cross', 'Ellipse']
# kernel = np.ones((3,3),np.uint)
# plt.figure(figsize=(15,15))
plt.subplot(2,2,1)
plt.imshow(mask, 'gray')
plt.title('Origin')

for i in range(3):
    dilation = cv2.dilate(mask, kernel[i]) # erode:침식
    plt.subplot(2,2,i+2)
    plt.imshow(dilation, 'gray')
    plt.title(title[i])
    plt.axis('off')

plt.tight_layout()
plt.show()