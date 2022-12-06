# 흑백 이미지 처리
import cv2
import matplotlib.pyplot as plt

image_path = 'cat.jpg'

# color -> gray. 이미지 대비 높이기
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)   # (374, 500) gray 여서 채널 생략.
image_enhanced = cv2.equalizeHist(image_gray)

# plot
fig, ax = plt.subplots(1,2, figsize=(10,5))
ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(image_enhanced, cmap='gray')
ax[1].set_title('Enhansed Image')
plt.show()