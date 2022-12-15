'''
opening : erosion -> dilation (to delate dot noise)
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Billiards.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3),np.uint8)

N = 5
idx = 1

for i in range(1, N+1):
    erosion = cv2.erode(mask, kernel, iterations=1) # 몇 번 수행할건지
    opening = cv2.dilate(erosion, kernel, iterations=1)
    f_opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    plt.subplot(N, 2, idx)
    idx += 1
    plt.imshow(opening, 'gray')
    plt.title(f'{i} Manual Opening')

    plt.subplot(N, 2, idx)
    plt.imshow(f_opening, 'gray')
    plt.title(f'{i} Function opening')
    idx += 1
plt.tight_layout()
plt.show()