# 컬러 이미지 처리
import cv2
import matplotlib.pyplot as plt

# 컬러 이미지 대비 높이기
# 방법 : RGB -> YUV 컬러 포맷으로 변환 -> equlizeHist() -> RGB

image_path = 'cat.jpg'

# BGR
image_bgr = cv2.imread(image_path)

# RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# YUV
image_yuv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YUV)

# 히스토그램 평활화 적용
image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])

# RGB로 변경
image_rgb_temp = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)

# plot
fig, ax = plt.subplots(1,2, figsize=(12,8))
ax[0].imshow(image_rgb)
ax[0].set_title('Original Image')
ax[1].imshow(image_rgb_temp)
ax[1].set_title('Enhansed Color Image')
plt.show()