import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Billiards.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(image, 230, 255, cv2.THRESH_BINARY_INV)

# kernel shape
kernel = np.ones((3,3), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=1)
erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing']
images = [image, mask, dilation, erosion, opening, closing]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

